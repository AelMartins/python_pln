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
                echo 'ja instalado'
            }
        }

        stage('Execução do Teste Levenshtein') {
            steps {
                sh 'python3 levenshtein_teste.py'
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
                sh "python3 chat_bot.py '${params.QUESTION}'"
            }
        }

        stage('Envio de e-mail') {
            steps {
                script {
                    def subject = "Pipeline: ${env.JOB_NAME} - ${env.BUILD_NUMBER}"
                    def body = "<p>Pipeline '${env.JOB_NAME} - ${env.BUILD_NUMBER}' completed.</p><p>Check console output at ${env.BUILD_URL}</p>"
                    sh "python3 send_email.py '${subject}' '${body}' '${RECIPIENT_EMAIL}'"
                }
            }
        }
    }
}
