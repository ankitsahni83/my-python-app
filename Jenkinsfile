pipeline {
    agent any

    environment {
        VENV_DIR = 'my-python-app-venv'
        VERSION = "0.1.${BUILD_NUMBER}"
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                rm -rf ${VENV_DIR}
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install setuptools wheel build coverage
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests with Coverage') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                coverage run -m unittest discover tests/
                coverage report
                coverage html
                coverage xml
                '''
            }
        }

        stage('Build Python Package') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                python -m build
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t my-python-app:${VERSION} --build-arg APP_VERSION=${VERSION} .
                '''
            }
        }

        stage('Deploy via Docker Compose') {
            steps {
                sh '''
                docker-compose down || true
                APP_VERSION=${VERSION} docker-compose up -d --force-recreate
                '''
            }
        }

        stage('Archive Build Artifacts') {
            steps {
                archiveArtifacts artifacts: 'dist/*.whl, dist/*.tar.gz', fingerprint: true
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

        stage('Test Docker Access') {
            steps {
                sh 'docker version'
            }
        }
     
    }

    post {
        success {
            echo "✅ Build, test, package, and deployment completed successfully."
        }
        failure {
            echo "❌ Something failed during the CI/CD pipeline."
        }
    }
}