
pipeline {
  agent any
  options { timestamps () }
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python hello_world.py'
      }
    }
  }
}
