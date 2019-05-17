import functions
import smtplib

from email.message import EmailMessage

def send(addr_to="leuckeju@katharineum.de", subject="", message="Nachricht"):

    SERVER, PORT, USER, PASSWORD = functions.parseCredentials()

    msg = EmailMessage()

    msg.set_content(message)
    msg["Subject"] = subject

    msg["From"] = USER
    msg["To"]   = addr_to

    connection = smtplib.SMTP(host=SERVER, port=PORT)
    connection.starttls()
    connection.login(USER, PASSWORD)
    connection.send_message(msg)
    connection.quit()
    print("Nachricht wurde gesendet")