pipeline {
    agent any

    environment {
        IMAGE_NAME = 'devops-demo'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install pytest
                    python -m pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Validate Helm Chart') {
            steps {
                sh '''
                    helm lint ./devops-demo
                    helm template devops-demo ./devops-demo
                '''
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully.'
        }
        failure {
            echo 'CI pipeline failed. Check the stage logs.'
        }
        always {
            cleanWs()
        }
    }
}
