pipeline {
agent any
  stages {




        stage('Install Python Virtual Environment') {
          steps{
            sh 'virtualenv --no-site-packages .'
          }
        }

    stage ("Install Application Dependencies") {
      steps{
        sh '''
            source bin/activate
            pip install -r requirements.txt
            deactivate
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
