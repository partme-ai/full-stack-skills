# Jenkins Pipeline with Docker

```groovy
pipeline {
    agent any
    environment {
        REGISTRY = 'docker.io/myorg'
        IMAGE_NAME = 'myapp'
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${BUILD_NUMBER}")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}:${BUILD_NUMBER}").inside {
                        sh 'npm test'
                    }
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    docker.withRegistry("https://${REGISTRY}", 'docker-hub-cred') {
                        docker.image("${IMAGE_NAME}:${BUILD_NUMBER}").push()
                        docker.image("${IMAGE_NAME}:${BUILD_NUMBER}").push('latest')
                    }
                }
            }
        }
    }
    post {
        always { cleanWs() }
    }
}
```
