pipeline {
    agent any

    stages {

        stage('Hello') {
            steps {
                echo 'Hello from Jenkins!'
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
    }
}
