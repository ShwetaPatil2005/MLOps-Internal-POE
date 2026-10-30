pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Pytest') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t mlops-uat-hello:latest .'
            }
        }

        stage('Run and Check Container') {
            steps {
                bat '''
                @echo off
                docker rm -f mlops-uat-hello 2>NUL
                docker run -d --name mlops-uat-hello -p 5001:5000 mlops-uat-hello:latest
                '''
                bat '''
                @echo off
                for /L %%i in (1,1,12) do (
                    curl.exe -fsS http://localhost:5001/health
                    if not errorlevel 1 (
                        echo Container health check passed.
                        exit /b 0
                    )
                    timeout /t 5 /nobreak >NUL
                )
                echo Container health check failed.
                docker logs mlops-uat-hello
                exit /b 1
                '''
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat 'python monitor.py'
            }
        }
    }

    post {
        always {
            bat 'docker rm -f mlops-uat-hello 2>NUL || exit /b 0'
        }
        success {
            echo 'MLOps UAT dry run completed successfully.'
        }
        failure {
            echo 'MLOps UAT dry run failed. Review Console Output.'
        }
    }
}
