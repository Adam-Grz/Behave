pipeline {
    agent any
    
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
            }, 
                "python" : {
                    sh 'docker pull ubuntu'
                    sh '''docker run -i -d --name ubuntuAG ubuntu
                        docker exec ubuntuAG apt-get -qq update
                        docker exec ubuntuAG apt-get -qq install -y python
                        docker exec ubuntuAG apt-get -qq install -y python-pip
                        docker exec ubuntuAG pip -q install selenium requests behave promise
                        docker exec ubuntuAG /bin/bash -c "apt-get -qq install git; git clone -q https://github.com/hugeinc/behave-parallel"
                        docker exec ubuntuAG /bin/bash -c "cd /behave-parallel"
                        docker exec ubuntuAG python /behave-parallel/setup.py --quiet install
                        docker exec ubuntuAG /bin/bash -c "cd .."
                        docker exec ubuntuAG scennumber=$(sed \'s/Scenario:/Scenario:\'$\'\n/g\' features/*.feature | grep -c "Scenario:")
                        docker exec ubuntuAG python behave-parallel/bin/behave-parallel --processes $scennumber --junit --junit-directory TestResults
                        docker exec ubuntuAG python bruteforce.py $TARGET_URL $LOGINS $PASSWORDS'''

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
