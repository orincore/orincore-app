pipeline {
  agent any

  environment {
    IMAGE_NAME = "orincore-flask-app"
    CONTAINER_NAME = "orincore-flask"
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
          sh "docker build -t ${IMAGE_NAME} ."
        }
      }
    }

    stage('Stop and Remove Existing Container') {
      steps {
        script {
          sh "docker stop ${CONTAINER_NAME} || true"
          sh "docker rm ${CONTAINER_NAME} || true"
        }
      }
    }

    stage('Run New Container') {
      steps {
        script {
          sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
        }
      }
    }
  }

  post {
    failure {
      echo "Deployment failed!"
      cleanWs()
    }
    success {
      echo "Deployment successful!"
    }
  }
}
