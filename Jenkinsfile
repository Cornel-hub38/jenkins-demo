pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building python application...'
                sh 'python3 -m compileall app.py'
            }
        }


        stage('Test') {
            steps {
                echo 'Running Python tests...'
                sh 'python3 -m venv .jenkins-venv'
                sh '.jenkins-venv/bin/pip install -r requirements.txt'
                sh '.jenkins-venv/bin/pytest'
            }
        }
        


        stage('System Information') {
            steps {
                sh 'whoami'
                sh 'hostname'
                sh 'git --version'
                sh 'java -version'
            }
        }

        stage('Package') {
            steps {
                echo 'Creating application package...'
                sh 'tar -czf jenkins-demo.tar.gz app.py requirements.txt'
            }
        }
    }


    post {
        success {
            archiveArtifacts artifacts: 'jenkins-demo.tar.gz', fingerprint: true
        }
    }
}
