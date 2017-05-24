pipeline {
    agent any
    
    stages{
        stage('cleanup') {
         steps {
          script {
           always {
           deleteDir()
                  }
                 }
               }
                         }

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
                    sh 'docker stop gatlingAG'
                    sh 'docker pull denvazh/gatling'
                    sh 'docker run --name gatlingAG -i -d denvazh/gatling'
                    sh 'docker cp RecordedSimulation.scala gatlingAG:/RecordedSimulation.scala'
                    sh 'ls'
            }, 
                "python" : {
                    sh 'docker stop ubuntuAG'
                    sh 'docker pull ubuntu'
                    sh 'docker run --name ubuntuAG -i ubuntu /bin/bash'
                    sh 'docker cp bruteforce.py ubuntuAG:/bruteforce.py'
                    sh 'docker cp logins.txt ubuntuAG:/logins.txt'
                    sh 'docker cp passwords.txt ubuntuAG:/passwords.txt'
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
