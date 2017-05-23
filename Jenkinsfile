pipeline {
    agent any
    
    stages{
        stage('Preparation') {
         steps{
          script{
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
                    sh 'bash ./test-python.sh' + params.TARGET_URL + params.LOGINS + params.PASSWORDS
            })
                       }
                 }
               }
         }
}
