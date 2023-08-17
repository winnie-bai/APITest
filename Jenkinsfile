pipeline{
    agent {
        label 'ubuntu'
    }
    stages{
        stage('api_test') {
            steps {
                sh '''cd $WORKSPACE
                      python3 -m pip install -r requirements.txt
                      python3 run.py'''
                allure includeProperties: false, jdk: '', results: [[path: '$WORKSPACE/allure-results']]
                archiveArtifacts artifacts: 'logs/*', followSymlinks: false
            }
        }
    }
}