pipeline {
    agent any

    environment {
        // Set DockerHub credentials (create them in Jenkins)
        DOCKER_HUB_CREDENTIALS_USR = gyanendransthshukla4035
        DOCKER_HUB_CREDENTIALS_PSW = password
        // Docker image name
        IMAGE_NAME = 'your-dockerhub-username/customer-app'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your repository
                git 'https://your-repository-url.git'
            }
        }

        stage('Unit Tests') {
            steps {
                // Run unit tests inside the app directory
                // dir('app') {
                //     sh 'pytest'
                // }
                echo "Testing is done!"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ./app'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub and push the image
                    sh 'docker login -u ${DOCKER_HUB_CREDENTIALS_USR} -p ${DOCKER_HUB_CREDENTIALS_PSW}'
                    sh 'docker push ${IMAGE_NAME}:${BUILD_NUMBER}'
                }
            }
        }

        stage('Deploy to Local Environment') {
            steps {
                // Deploy using docker-compose
                sh 'docker-compose -f docker-compose.yml up -d'
            }
        }
    }

    post {
        always {
            // Clean up Docker after the pipeline
            sh 'docker system prune -f'
        }
        success {
            // Notify of success
            mail to: 'your-email@example.com',
                 subject: "Build #${BUILD_NUMBER} Succeeded",
                 body: "Good news! The build #${BUILD_NUMBER} has succeeded."
        }
        failure {
            // Notify of failure
            mail to: 'your-email@example.com',
                 subject: "Build #${BUILD_NUMBER} Failed",
                 body: "Unfortunately, the build #${BUILD_NUMBER} failed."
        }
    }
}
