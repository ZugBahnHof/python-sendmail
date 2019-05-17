import functions
import smtplib

def send(addr_to="", message="Nachricht"):

    SERVER, PORT, USER, PASSWORD = functions.parseCredentials()

    connection = smtplib.SMTP(host=SERVER, port=PORT)
    connection.starttls()
    connection.login(USER, PASSWORD)
    connection.sendmail(from_addr=USER, to_addrs=addr_to, msg=message)
    connection.quit()
    print("Nachricht wurde gesendet")