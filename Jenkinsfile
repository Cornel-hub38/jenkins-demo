pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Starting build...'
                sh 'echo Building application'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests... SCM 5 minute polling works, Hello from Jenkinsfile'
                sh 'echo Running tests'
                sh 'test -f Jenkinsfile'
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
                echo 'Creating package...'
                sh 'tar -czf jenkins-demo.tar.gz Jenkinsfile'
            }
        }
    }


    post {
        success {
            archiveArtifacts artifacts: 'jenkins-demo.tar.gz', fingerprint: true
        }
    }
}
