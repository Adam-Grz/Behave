pipeline {
    agent any
    
    stages{
        stage('Preparation') {
         steps{
          script{
            sh 'docker run -d -p 8080:8080 -t webgoat/webgoat-7.1'
                }
              }
          }

        stage('test') {
         steps {
          script {
            parallel (
                "gatling" : {
                    sh 'docker cp RecordedSimulation.scala denvazh/gatling:/RecordedSimulation.scala'
                    sh 'docker run -it -m denvazh/gatling /bin/bash'
                    sh 'ls'
            }, 
                "python" : {
                    sh 'bash ./test-python.sh'
            })
                       }
                 }
               }
        stage('cleanup') {
         steps {
          scripts {
           deleteDir()
                  }
               }
                         }
         }
}
