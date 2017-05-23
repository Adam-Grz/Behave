pipeline {
    agent any
    
    stages{
        stage('Preparation') {
            sh 'prep.sh'
          }
}
    stages{
        stage('test') {
            parallel gatling: {
            sh 'test-gatling.sh'
            }, python: {
            sh 'test-python.sh' + params.TARGET_URL + params.LOGINS + params.PASSWORDS
            },
    failFast: false
                      }
           }
}
