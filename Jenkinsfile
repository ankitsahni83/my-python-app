pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    environment {
        PYTHON_BIN = '/usr/bin/python3'
        PIP_BIN = '/usr/bin/pip3'
        VENV_DIR = 'my-python-app-venv'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                python -m venv $VENV_DIR
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                python -m unittest discover tests/
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Build successful"
        }
        failure {
            echo "❌ Build failed"
        }
    }
}