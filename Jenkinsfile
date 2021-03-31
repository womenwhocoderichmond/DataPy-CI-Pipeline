pipeline {
agent {
    docker { image 'python:3.9.1' }
}

stages {
    stage ("Install Application Dependencies") {
            steps{
                sh '''
                   pip install -r requirements.txt
                   '''
            }
    }

    stage('Linting') {
            steps {
                   sh '''
                      pylint simple_rest.py
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
            sh '''
               echo $BUILD_NUMBER
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
        sh  '''
            '''
        }
      }
    }
}
