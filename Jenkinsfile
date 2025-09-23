pipeline {
    agent any

    environment {
        VENV_DIR = 'my-python-app-venv'
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                rm -rf ${VENV_DIR}
                python3 -m venv $VENV_DIR
                . $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests with Coverage') {
            steps {
                sh '''
                . $VENV_DIR/bin/activate
                coverage run -m unittest discover tests/
                coverage report
                coverage html
                coverage xml
                '''
            }
        }

        stage('Publish Coverage Report') {
            steps {
                publishHTML(target: [
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])
            }
        }
    }

    post {
        success {
            echo "✅ Build and tests with coverage completed successfully."
        }
        failure {
            echo "❌ Build or tests with coverage failed."
        }
    }
}