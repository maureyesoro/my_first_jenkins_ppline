pipeline {
    agent any
    stages {
        stage('build') {
            when {
                expression {
                    BRANCH_NAME == 'main'
                }
            }
            steps {
                echo 'building the application'
            }
        }
        stage('test') {
            when {
                expression {
                    BRANCH_NAME == 'feature1' || BRANCH_NAME == 'feature2'
                }
            }
            steps {
                echo 'testing the application'
            }
        }
    }
    post {
        always {
            echo 'finished all stages'
        }
        succes {
            echo 'jenkins pipeline successfull'
        }
        failure {
            echo 'jenkins pipeline failed'
        }
    }
}