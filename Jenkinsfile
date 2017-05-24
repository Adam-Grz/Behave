pipeline {
    agent any
    
    stages{
        stage('Preparation') {
         steps{
          script{
            sh 'docker run -d -p 8080:8080 webgoat/webgoat-7.1'
                }
              }
          }

        stage('test') {
         steps {
          script {
            parallel (
                "gatling" : {
                    sh 'docker pull denvazh/gatling'
                    sh 'docker run -d denvazh/gatling'
                    sh 'docker cp RecordedSimulation.scala denvazh/gatling:/RecordedSimulation.scala'
                    sh 'ls'
            }, 
                "python" : {
                    sh 'docker pull ubuntu'
                    sh 'docker run -i ubuntu /bin/bash'
                    sh 'docker cp bruteforce.py ubuntu:/bruteforce.py'
                    sh 'docker cp logins.txt ubuntu:/logins.txt'
                    sh 'docker cp passwords.txt ubuntu:/passwords.txt'
                    sh 'apt-get update'
                    sh 'apt-get -y install python'
                    sh 'apt-get -y install pip'
                    sh 'pip -q install selenium requests behave promise git'
                    sh 'git clone -q https://github.com/hugeinc/behave-parallel'
                    sh 'cd behave-parallel'
                    sh 'python setup.py --quiet install'
                    sh 'cd ..'
                    sh 'python behave-parallel/bin/behave-parallel --processes 4 --junit --junit-directory TestResults' 
                    sh 'python bruteforce.py $TARGET_URL $LOGINS $PASSWORDS'

            })
                       }
                 }
               }
        stage('cleanup') {
         steps {
          script {
           always {
           deleteDir()
                  }
                 }
               }
                         }
         }
}
