pipeline {
    agent any
    
    stages{
        stage('Preparation') {
         steps{
          script{
            sh 'docker run -d -p 8080:8080 webgoat/webgoat-7.1'
            sh 'docker pull adamgrz/my-ubuntu'
            sh 'docker build -t aa -f Dockerfile .'
            sh 'docker run -d --name selenium aa'
            sh 'docker exec selenium ps aux'
                }
              }
          }

        stage('test') {
         steps {
          script {
            parallel (
                "gatling" : {
                    sh '''docker run -i -d --net=host --name gatlingAG adamgrz/my-ubuntu
                          /*docker exec gatlingAG /bin/bash -c "./gatling/bin/gatling.sh -m"
                          docker cp gatlingAG:/gatling/TestResults .*/'''
            }, 
                "python" : {
                    sh '''docker run -i -d --net=host --name ubuntuAG adamgrz/my-ubuntu
                        /*docker cp features/environment.py ubuntuAG:/features/
                        docker exec ubuntuAG /bin/bash -c "./sed.sh"
                        docker exec ubuntuAG python bruteforce.py $TARGET_URL $LOGINS $PASSWORDS
                        docker cp ubuntuAG:/PythonResults .
                        docker cp ubuntuAG:/bruteforceresult.txt .*/'''
                     junit '**/PythonResults/*.xml'
            },
                "javascript" : {
                    sh 'docker exec selenium /bin/bash -c "cd JavaScript; protractor run.js"'
                    sh 'docker cp selenium:/JavaScript/JStests.log .'
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
