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
                    sh 'docker run -m denvazh/gatling ./gatling.sh'
                    sh 'docker cp RecordedSimulation.scala denvazh/gatling:/RecordedSimulation.scala'
                    sh 'ls'
            }, 
                "python" : {
                    sh 'docker pull themcmurder/ubuntu-python-pip'
                    sh 'docker run themcmurder/ubuntu-python-pip'
                    sh 'docker cp bruteforce.py themcmurder/ubuntu-python-pip:/bruteforce.py'
                    sh 'docker cp logins.txt themcmurder/ubuntu-python-pip:/logins.txt'
                    sh 'docker cp passwords.txt themcmurder/ubuntu-python-pip:/passwords.txt'
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
