pipeline {
    agent any

    parameters {
        string(name: 'QUESTION', defaultValue: '', description: 'Faça uma pergunta ao chat-bot!')
    }

    environment {
        RECIPIENT_EMAIL = 'samuelluizmartinsdosantos@gmail.com'
    }

    stages {
        stage('Preparação do Ambiente') {
            steps {
                sh 'pip install -r requisitos.txt'
            }
        }

        stage('Execução do Teste Levenshtein') {
            steps {
                sh 'python levenshtein_teste.py'
            }
        }

        stage('Verificação do Arquivo de Perguntas') {
            steps {
                script {
                    if (fileExists('perguntas.txt')) {
                        echo 'Arquivo perguntas.txt encontrado!'
                    } else {
                        error('Arquivo perguntas.txt não encontrado. Interrompendo o pipeline.')
                    }
                }
            }
        }

        stage('Execução do Chatbot') {
            steps {
                sh 'python chat_bot.py'
            }
        }
    }

    post {
        success {
            steps {
                script {
                    sh """
                        python send_email.py \
                            "Pipeline Success: ${env.JOB_NAME} - ${env.BUILD_NUMBER}" \
                            "<p>Pipeline '${env.JOB_NAME} - ${env.BUILD_NUMBER}' succeeded.</p><p>Check console output at ${env.BUILD_URL}</p>" \
                            "${RECIPIENT_EMAIL}"
                    """
                }
            }
        }
        failure {
            steps {
                script {
                    sh """
                        python send_email.py \
                            "Pipeline Failed: ${env.JOB_NAME} - ${env.BUILD_NUMBER}" \
                            "<p>Pipeline '${env.JOB_NAME} - ${env.BUILD_NUMBER}' failed.</p><p>Check console output at ${env.BUILD_URL}</p>" \
                            "${RECIPIENT_EMAIL}"
                    """
                }
            }
        }
    }
}
