pipeline {
    agent any
    
    stages{
        stage('Preparation') {
         steps{
          script{
            sh 'docker run -d -p 8080:8080 webgoat/webgoat-7.1'
            sh 'docker pull adamgrz/gatling-ubuntu'
                }
              }
          }

        stage('test') {
         steps {
          script {
            parallel (
                "gatling" : {
                    sh '''docker run -i -d --net=host --name gatlingAG adamgrz/gatling-ubuntu
                          docker exec gatlingAG /bin/bash -c "./gatling/bin/gatling.sh -m"
                          docker cp gatlingAG:/gatling/TestResults .'''
            }, 
                "python" : {
                    sh '''docker run -i -d --net=host --name ubuntuAG ubuntu
                        docker cp sed.sh ubuntuAG:/
                        docker cp features ubuntuAG:/
                        docker cp bruteforce.py ubuntuAG:/
                        docker cp logins.txt ubuntuAG:/
                        docker cp passwords.txt ubuntuAG:/
                        docker exec ubuntuAG apt-get -qq update
                        docker exec ubuntuAG apt-get -qq install -y python
                        docker exec ubuntuAG apt-get -qq install -y python-pip
                        docker exec ubuntuAG pip install selenium requests behave promise
                        docker exec ubuntuAG /bin/bash -c "apt-get install -y apt-utils; apt-get -qq install -y git; git clone -q https://github.com/hugeinc/behave-parallel"
                        docker exec ubuntuAG /bin/bash -c "apt-get install -y firefox"
                        docker exec ubuntuAG /bin/bash -c "cd /behave-parallel/; python setup.py --quiet install; cd .."
                        docker cp geckodriver ubuntuAG:/usr/local/bin/
                        docker exec ubuntuAG /bin/bash -c "chmod 777 sed.sh; ./sed.sh"
                        docker exec ubuntuAG python bruteforce.py $TARGET_URL $LOGINS $PASSWORDS
                        docker cp ubuntuAG:/PythonResults .
                        docker cp ubuntuAG:/bruteforceresult.txt .'''
                     junit '**/PythonResults/*.xml'
            })
                       }
                 }
               }
         }
    post {
      always {
            sh 'docker stop $(docker ps -a -q)'
            sh 'docker rm $(docker ps -a -q)'
             }
         }
}
