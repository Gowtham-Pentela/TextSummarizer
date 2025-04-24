pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'text-summarizer:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    try {
                        checkout scm
                    } catch (Exception e) {
                        error "Checkout failed: ${e.message}"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        docker.build(DOCKER_IMAGE)
                    } catch (Exception e) {
                        error "Docker build failed: ${e.message}"
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    try {
                        withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                            docker.image(DOCKER_IMAGE).push()
                        }
                    } catch (Exception e) {
                        error "Push to Docker Hub failed: ${e.message}"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    try {
                        echo 'Deploying application...'
                        // Add deployment steps here
                    } catch (Exception e) {
                        error "Deployment failed: ${e.message}"
                    }
                }
            }
        }
    }
}