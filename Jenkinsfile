pipeline {
agent any
  stages {


    stage ("Install Application Dependencies") {
      steps{
        sh '''
            pip install --user -r requirements.txt
           '''
      }
    }



    stage('test') {
      steps {
         withPythonEnv('python') {
          python test.py
      }
      }
      
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}
