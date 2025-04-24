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
                        // Stop any running container with the same name
                        sh 'docker stop text-summarizer || true && docker rm text-summarizer || true'
                        // Run the new container
                        sh 'docker run -d --name text-summarizer -p 8080:8080 text-summarizer:latest'
                    } catch (Exception e) {
                        error "Deployment failed: ${e.message}"
                    }
                }
            }
        }
    }
}