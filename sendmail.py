import functions
import smtplib

from email.message import EmailMessage

def send(addr_to="", subject="", message=""):

    if len(addr_to) > 0 and len(subject) > 0 and len(message) > 0:
        pass
    else:
        raise AttributeError("Receiver, subject and message must be given!")

    SERVER, PORT, USER, PASSWORD = functions.parseCredentials()

    msg = EmailMessage()

    msg.set_content(message)
    msg["Subject"] = subject

    msg["From"] = USER
    msg["To"]   = addr_to

    connection = smtplib.SMTP(host=SERVER, port=PORT)
    connection.starttls()
    print("Connecting to {}...".format(SERVER))
    connection.login(USER, PASSWORD)
    print("Sending message...")
    connection.send_message(msg)
    connection.quit()
    functions.printInGreen("Success")