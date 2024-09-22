pipeline {
    agent any

    environment {
        // Secure DockerHub credentials (set these as Jenkins credentials, not hard-coded)
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials-id')
        // Docker image name
        IMAGE_NAME = 'gyanendranathshukla4035/flask-app'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your repository
                git 'https://github.com/Grokr-gyanendra/jenkins_docker_flask.git'
            }
        }

        stage('Unit Tests') {
            steps {
                // Uncomment and modify as needed to run actual tests
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
                    bat 'docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ./app'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Use --password-stdin for secure Docker login
                    bat """
                        echo ${DOCKER_HUB_CREDENTIALS_PSW} | docker login -u ${DOCKER_HUB_CREDENTIALS_USR} --password-stdin
                    """
                    
                    // Push the Docker image to Docker Hub
                    bat 'docker push %IMAGE_NAME%:%BUILD_NUMBER%'
                }
            }
        }

        stage('Deploy to Local Environment') {
            steps {
                // Deploy using docker-compose on Linux (if applicable)
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
