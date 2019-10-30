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

    stage('Linting') {
      steps {
      sh '''

         '''
      }
      }


    stage('Unit Test') {
      steps {
      sh '''
          python test.py
         '''
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
      }

      stage('Building artifact') {
        steps {
        sh '''
           '''
        }

        }
        stage('Storing Artifact') {
          steps {
          sh '''
             '''
          }
          }



}
}
