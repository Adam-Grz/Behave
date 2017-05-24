pipeline {
    agent any
    
    stages{
        stage('Preparation') {
         steps{
          script{
            sh 'docker run -d -p 8080:8080 webgoat/webgoat-7.1'
                }
              }
          }

        stage('test') {
         steps {
          script {
            parallel (
                "gatling" : {
                    sh 'docker pull denvazh/gatling'
                    sh 'docker run -m -d denvazh/gatling'
                    sh 'docker exec cp RecordedSimulation.scala denvazh/gatling:/RecordedSimulation.scala'
                    sh 'ls'
            }, 
                "python" : {
                    sh 'docker pull themcmurder/ubuntu-python-pip'
                    sh 'docker run -d themcmurder/ubuntu-python-pip'
                    sh 'docker exec cp bruteforce.py themcmurder/ubuntu-python-pip:/bruteforce.py'
                    sh 'docker exec cp logins.txt themcmurder/ubuntu-python-pip:/logins.txt'
                    sh 'docker exec cp passwords.txt themcmurder/ubuntu-python-pip:/passwords.txt'
                    sh 'python bruteforce.py $TARGET_URL $LOGINS $PASSWORDS'

            })
                       }
                 }
               }
        stage('cleanup') {
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
