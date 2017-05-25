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
                    sh 'docker pull ubuntu'
                    sh '''docker run -i -d --name gatlingAG ubuntu
                          docker cp gatling gatlingAG:/
                          docker exec gatlingAG apt-get -qq update
                          docker exec gatlingAG apt-get -qq install default-jdk
                          docker exec gatlingAG /bin/bash -c "./gatling/bin/gatling.sh -m"'''
            }, 
                "python" : {
                    sh 'docker pull ubuntu'
                    sh '''docker run -i -d --net=host --name ubuntuAG ubuntu
                        docker cp sed.sh ubuntuAG:/
                        docker cp features ubuntuAG:/
                        docker cp geckodriver ubuntuAG:/
                        docker cp geckodriver ubuntuAG:/features/
                        docker cp geckodriver ubuntuAG:/features/steps/
                        docker cp bruteforce.py ubuntuAG:/
                        docker cp logins.txt ubuntuAG:/
                        docker cp passwords.txt ubuntuAG:/
                        docker exec ubuntuAG apt-get -qq update
                        docker exec ubuntuAG apt-get -qq install -y python
                        docker exec ubuntuAG apt-get -qq install -y python-pip
                        docker exec ubuntuAG pip install selenium requests behave promise
                        docker exec ubuntuAG /bin/bash -c "apt-get install -y apt-utils; apt-get -qq install -y git; git clone -q https://github.com/hugeinc/behave-parallel"
                        docker exec ubuntuAG /bin/bash -c "apt-get install -y firefox"
                        docker exec ubuntuAG /bin/bash -c "export PATH='/'"
                        docker exec ubuntuAG /bin/bash -c "export PATH='/features/'"
                        docker exec ubuntuAG /bin/bash -c "echo $PATH"
                        docker exec ubuntuAG /bin/bash -c "cd /behave-parallel/; python setup.py --quiet install; cd .."
                        docker cp geckodriver ubuntuAG:/behave-parallel/
                        docker cp geckodriver ubuntuAG:/behave-parallel/bin/
                        docker exec ubuntuAG /bin/bash -c "chmod 777 sed.sh; ./sed.sh"
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
