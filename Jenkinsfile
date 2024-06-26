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
    }

    post {
        success {
            emailext (
                to: "${RECIPIENT_EMAIL}",
                subject: "Pipeline Success: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                body: """<p>Pipeline '${env.JOB_NAME} - ${env.BUILD_NUMBER}' succeeded.</p>
                         <p>Check console output at ${env.BUILD_URL}</p>""",
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                to: "${RECIPIENT_EMAIL}",
                subject: "Pipeline Failed: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                body: """<p>Pipeline '${env.JOB_NAME} - ${env.BUILD_NUMBER}' failed.</p>
                         <p>Check console output at ${env.BUILD_URL}</p>""",
                mimeType: 'text/html'
            )
        }
    }
}
