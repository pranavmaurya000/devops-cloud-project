pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t devops-backend ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t devops-frontend ./frontend'
            }
        }

        stage('Test Backend') {
            steps {
                sh 'docker run -d --name ci-backend -p 5001:5000 devops-backend'
                sh 'sleep 5'
                sh 'curl -f http://localhost:5001/health'
                sh 'docker stop ci-backend'
                sh 'docker rm ci-backend'
            }
        }
    }

    post {

        success {
            echo '✅ CI Pipeline completed successfully!'
        }

        failure {
            echo '❌ CI Pipeline failed!'
        }

        always {
            sh 'docker rm -f ci-backend 2>/dev/null || true'
        }
    }
}