import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = 'samuelluizmartinsdossantos@gmail.com'
    from_password = 'E.E.HomeroA1'

    # Configuração do servidor SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)

    # Construção da mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    # Envio do e-mail
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Uso: python send_email.py <assunto> <corpo> <email_destino>")
        sys.exit(1)

    subject = sys.argv[1]
    body = sys.argv[2]
    to_email = sys.argv[3]

    send_email(subject, body, to_email)
