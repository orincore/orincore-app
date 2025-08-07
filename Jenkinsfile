pipeline {
  agent any

  environment {
    IMAGE_NAME = "orincore-flask-app"
    CONTAINER_NAME = "orincore-flask"
    CONTAINER_PORT = "5000"
    HOST_PORT = "5000"
  }

  stages {
    stage('Clone Repository') {
      steps {
        git branch: 'main', url: 'https://github.com/orincore/orincore-app.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          sh "sudo docker build -t ${IMAGE_NAME} ."
        }
      }
    }

    stage('Stop and Remove Existing Container') {
      steps {
        script {
          sh """
            if sudo docker ps -a --format '{{.Names}}' | grep -Eq '^${CONTAINER_NAME}\$'; then
              sudo docker stop ${CONTAINER_NAME}
              sudo docker rm ${CONTAINER_NAME}
            fi
          """
        }
      }
    }

    stage('Run New Container') {
      steps {
        script {
          sh "sudo docker run -d -p ${HOST_PORT}:${CONTAINER_PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
        }
      }
    }
  }

  post {
    always {
      echo 'Cleaning up workspace...'
      cleanWs()
    }
    failure {
      echo 'Deployment failed!'
    }
    success {
      echo "Application deployed successfully on port ${HOST_PORT}"
    }
  }
}
