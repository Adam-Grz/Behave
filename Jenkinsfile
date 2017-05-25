pipeline {
    agent any
    
    gatlingArchive()
    
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
                    sh 'docker ps'

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
