pipeline {
agent any
  stages {


    stage ("Install Application Dependencies") {
      steps{
        sh '''
            pip install -r requirements.txt
           '''
      }
    }



    stage('test') {
      steps {
      sh '''
          source bin/activate
          sh 'python test.py'
          deactivate
         '''
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}
