pipeline {
    agent any
    
    stages{
        stage('Preparation') {
         steps{
          script{
            sh 'docker run -d -p 8080:8080 -t webgoat/webgoat-7.1'
            sh 'bash ./prep.sh'
                }
              }
          }

        stage('test') {
         steps {
          script {
            parallel (
                "gatling" : {
                    sh 'bash ./test-gatling.sh'
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
