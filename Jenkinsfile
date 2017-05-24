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
                    sh 'docker stop gatlingAG'
                    sh 'docker rm gatlingAG'
                    sh 'docker pull denvazh/gatling'
                    sh 'docker run --name gatlingAG denvazh/gatling'
                    sh 'docker cp gatling gatlingAG:/'
                    sh 'docker run --name gatlingAG denvazh/gatling ./gatling/bin/gatling.sh'
            }, 
                "python" : {
                    sh 'docker stop ubuntuAG'
                    sh 'docker rm ubuntuAG'
                    sh 'docker pull ubuntu'
                    sh 'docker run --name ubuntuAG ubuntu /bin/bash'
                    sh 'docker cp bruteforce.py ubuntuAG:/bruteforce.py'
                    sh 'docker cp logins.txt ubuntuAG:/logins.txt'
                    sh 'docker cp passwords.txt ubuntuAG:/passwords.txt'
                    sh 'docker run ubuntu apt-get update'
                    sh 'docker run ubuntu apt-get -y install python'
                    sh 'docker run ubuntu apt-get -y install pip'
                    sh 'docker run ubuntu pip -q install selenium requests behave promise git'
                    sh 'docker run ubuntu git clone -q https://github.com/hugeinc/behave-parallel'
                    sh 'docker run ubuntu cd behave-parallel'
                    sh 'docker run ubuntu python setup.py --quiet install'
                    sh 'docker run ubuntu cd ..'
                    sh 'docker run ubuntu python behave-parallel/bin/behave-parallel --processes 4 --junit --junit-directory TestResults' 
                    sh 'docker run ubuntu python bruteforce.py $TARGET_URL $LOGINS $PASSWORDS'

            })
                       }
                 }
               }
        stage('cleanup2') {
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
