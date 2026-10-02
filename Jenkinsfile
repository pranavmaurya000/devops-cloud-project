pipeline {

    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        AWS_ACCOUNT_ID = '172575864548'
        ECR_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
    }

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
            }
        }

        stage('Push Images to ECR') {
            steps {
                withCredentials([
                    [$class: 'AmazonWebServicesCredentialsBinding',
                     credentialsId: 'aws-ecr-credentials']
                ]) {

                    sh '''
                        aws ecr get-login-password --region $AWS_REGION |
                        docker login --username AWS --password-stdin $ECR_REGISTRY

                        docker tag devops-backend:latest \
                        $ECR_REGISTRY/devops-backend:latest

                        docker tag devops-frontend:latest \
                        $ECR_REGISTRY/devops-frontend:latest

                        docker push $ECR_REGISTRY/devops-backend:latest
                        docker push $ECR_REGISTRY/devops-frontend:latest
                    '''
                }
            }
        }
    }

    post {

        always {
            sh 'docker rm -f ci-backend 2>/dev/null || true'
        }

        success {
            echo '✅ CI/CD pipeline completed successfully!'
        }

        failure {
            echo '❌ Pipeline failed!'
        }
    }
}