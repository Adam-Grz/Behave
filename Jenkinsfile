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
                    sh '''docker run -i -d --name ubuntuAG ubuntu
                        docker cp sed.sh ubuntuAG:/
                        docker cp features ubuntuAG:/
                        docker exec ubuntuAG apt-get -qq update
                        docker exec ubuntuAG apt-get -qq install -y python
                        docker exec ubuntuAG apt-get -qq install -y python-pip
                        docker exec ubuntuAG pip install selenium requests behave promise
                        docker exec ubuntuAG /bin/bash -c "apt-get install -y apt-utils; apt-get -qq install -y git; git clone -q https://github.com/hugeinc/behave-parallel"
                        docker exec ubuntuAG /bin/bash -c "cd /behave-parallel/; python setup.py --quiet install; cd .."
                        docker exec ubuntuAG /bin/bash -c "chmod 777 sed.sh; ./sed.sh"
                        docker exec ubuntuAG python behave-parallel/bin/behave-parallel --processes $scennumber --junit --junit-directory TestResults
                        docker exec ubuntuAG python bruteforce.py $TARGET_URL $LOGINS $PASSWORDS'''

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
