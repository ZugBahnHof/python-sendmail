import functions
import smtplib

def send(addr_to="", message):

    SERVER, PORT, USER, PASSWORD = functions.parseCredentials()

    connection = smtplib.SMTP(host=SERVER, port=PORT)
    connection.sendmail(USER, addr_to, message)
    connection.quit()