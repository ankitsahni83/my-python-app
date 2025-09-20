pipeline {
    agent any

    environment {
        VENV_DIR = 'my-python-app-venv'
    }

    stages {
        stage('Clone') {
            steps {
                // Jenkins auto-clones when using "Pipeline from SCM", but keep this if doing scripted SCM
                checkout scm
            }
        }

        stage('Set up Python Env') {
            steps {
                sh '''
                python3 -m venv $VENV_DIR
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
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
            echo "✅ Build and tests completed successfully."
        }
        failure {
            echo "❌ Build or tests failed."
        }
    }
}