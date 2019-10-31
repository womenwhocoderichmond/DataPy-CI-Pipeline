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

      stage('Build Artifact') {
                  when {
                      expression {
                          currentBuild.result == null || currentBuild.result == 'SUCCESS'
                      }
                  }
                  steps {
                      sh  '''
                              python setup.py bdist_wheel
                          '''
                  }
                  post {
                      always {
                          // Archive unit tests for the future
                          archiveArtifacts allowEmptyArchive: true, artifacts: 'dist/*whl', fingerprint: true
                      }
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
