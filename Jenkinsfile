pipeline {
    agent any
    
    stages{
        stage('Preparation') {
         steps{
          script{
            sh 'docker stop $(docker ps -a -q)'
            sh 'docker rm $(docker ps -a -q)'
            sh 'docker run -d -p 8080:8080 webgoat/webgoat-7.1'
                }
              }
          }

        stage('test') {
         steps {
          script {
            parallel (
                "gatling" : {
                    sh 'docker ps'
            }, 
                "python" : {
                    sh 'docker pull ubuntu'
                    sh 'docker run --name ubuntuAG ubuntu /bin/bash'
                    sh 'docker cp bruteforce.py ubuntuAG:/bruteforce.py'
                    sh 'docker cp logins.txt ubuntuAG:/logins.txt'
                    sh 'docker cp passwords.txt ubuntuAG:/passwords.txt'
                    sh 'docker cp behave-parallel ubuntuAG:/'
                    sh '''docker run ubuntuAG apt-get update;
                        docker run ubuntuAG pip -q install selenium requests behave promise;
                        docker run ubuntuAG cd behave-parallel;
                        docker run ubuntuAG python setup.py --quiet install;
                        docker run ubuntuAG cd ..;
                        docker run ubuntuAG scennumber=$(sed \'s/Scenario:/Scenario:\'$\'\n/g\' features/*.feature | grep -c "Scenario:");
                        docker run ubuntuAG python behave-parallel/bin/behave-parallel --processes $scennumber --junit --junit-directory TestResults;
                        docker run ubuntuAG python bruteforce.py $TARGET_URL $LOGINS $PASSWORDS'''

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
