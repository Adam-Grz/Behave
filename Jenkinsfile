pipeline {
    agent any
    
    stages{
        stage('Preparation') {
         steps{
          script{
            sh './prep.sh'
                }
              }
          }

        stage('test') {
         steps {
          script {
            parallel (
                "gatling" : {
                    sh './test-gatling.sh'
            }, 
                "python" : {
                    sh './test-python.sh' + params.TARGET_URL + params.LOGINS + params.PASSWORDS
            })
                       }
                 }
               }
         }
}
