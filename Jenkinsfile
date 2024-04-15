pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("data-processing-app:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("data-processing-app:${env.BUILD_NUMBER}").run("--entrypoint=''")
                    sh 'docker exec `docker ps -q -f "ancestor=data-processing-app:${env.BUILD_NUMBER}"` pytest'
                }
            }
        }

        stage('Deploy to Cloud') {
            steps {
                script {
                    sh '''
                        # Push Docker image to Docker registry (if needed)
                        docker login -u username -p password
                        docker push username/data-processing-app:${env.BUILD_NUMBER}
                        
                        # Deploy using Terraform
                        cd terraform/
                        terraform init
                        terraform apply -auto-approve
                    '''
                }
            }
        }
    }
}
