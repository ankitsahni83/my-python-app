pipeline {
    agent any

    environment {
        PYTHON_BIN = 'python3'
        VENV_DIR = 'my-python-app-venv'
    }

    stages {
        stage('Debug Info') {
            steps {
                sh '''
                echo "✅ Python version:"
                python3 --version
                which python3
                echo "✅ Current directory:"
                pwd
                echo "✅ Listing current files:"
                ls -alh
                '''
            }
        }

        stage('Create Virtual Env') {
            steps {
                sh '''
                echo "🧹 Cleaning up any existing venv..."
                rm -rf ${VENV_DIR}
                echo "🐍 Creating new virtual environment..."
                ${PYTHON_BIN} -m venv ${VENV_DIR}
                echo "✅ Virtualenv created. Listing contents:"
                ls -l ${VENV_DIR}/bin
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt || echo "⚠️ requirements.txt not found or failed"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
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