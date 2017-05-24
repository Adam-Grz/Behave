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
                        docker exec echo "Hello from container!"
                        apt-get update;
                        pip -q install selenium requests behave promise;
                        cd behave-parallel;
                        python setup.py --quiet install;
                        cd ..;
                        scennumber=$(sed \'s/Scenario:/Scenario:\'$\'\n/g\' features/*.feature | grep -c "Scenario:");
                         python behave-parallel/bin/behave-parallel --processes $scennumber --junit --junit-directory TestResults;
                        python bruteforce.py $TARGET_URL $LOGINS $PASSWORDS'''

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
