pipeline {
    agent any
    
    stages{
        stage('Preparation') {
         steps{
          script{
            sh 'docker run -d -p 8080:8080 webgoat/webgoat-7.1'
            sh 'docker pull adamgrz/my-ubuntu'
                }
              }
          }

        stage('test') {
         steps {
          script {
            parallel (
                "gatling" : {
                    sh '''docker run -i -d --net=host --name gatlingAG adamgrz/my-ubuntu
                          docker exec gatlingAG /bin/bash -c "./gatling/bin/gatling.sh -m"
                          docker cp gatlingAG:/gatling/TestResults .'''
            }, 
                "python" : {
                    sh '''docker run -i -d --net=host --name ubuntuAG adamgrz/my-ubuntu
                        docker cp features/environment.py ubuntuAG:/features/
                        docker exec ubuntuAG /bin/bash -c "./sed.sh"
                        docker exec ubuntuAG python bruteforce.py $TARGET_URL $LOGINS $PASSWORDS
                        docker cp ubuntuAG:/PythonResults .
                        docker cp ubuntuAG:/bruteforceresult.txt .'''
                     junit '**/PythonResults/*.xml'
            },
                "javascript" : {
                    sh 'docker run -it -d --net=host --name jsAG adamgrz/my-ubuntu
                    sh 'Xvfb -ac :99 -screen 0 1280x1024x16 &'
                    sh 'export DISPLAY=:99'
                    sh 'webdriver-manager start /dev/null 2>&1'
                    sh '''docker exec jsAG /bin/bash -c "cd JavaScript; protractor run.js > JStests.log"
                        docker cp jsAG:/JavaScript/JStests.log .'''
            }
                      )
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
