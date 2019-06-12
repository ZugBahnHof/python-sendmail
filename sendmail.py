import functions
import smtplib

# from email.message import EmailMessage
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# subject = "An email with attachment from Python"
# body = "This is an email with attachment sent from Python"
# sender_email = "my@gmail.com"
# receiver_email = "your@gmail.com"
# password = input("Type your password and press enter:")



def send(password, addr_to="", subject="", message="", filename=None):

    if len(addr_to) > 0 and len(subject) > 0 and len(message) > 0:
        pass
    else:
        raise AttributeError("Receiver, subject and message must be given!")

    SERVER, PORT, USER, PASSWORD = functions.parseCredentials(pwd=password)

    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg["From"] = USER
    msg["To"] = addr_to
    msg["Subject"] = subject

    # Add body to email
    msg.attach(MIMEText(message, "plain"))

    if filename is not None:

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            print("Opening attachment file…")
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        print("Adding attachment file to the email…")

        # Add attachment to message and convert message to string
        msg.attach(part)

    text = msg.as_string()


    connection = smtplib.SMTP(host=SERVER, port=PORT)
    connection.starttls()
    print("Connecting to {}...".format(SERVER))
    connection.login(USER, PASSWORD)
    print("Sending message...")
    connection.sendmail(USER, addr_to, text)
    connection.quit()
    functions.printInGreen("Success")