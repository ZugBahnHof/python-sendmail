# Not a real TUI, just a bunch of prints and inputs
from sendmail import send
from receivemail import getMails
import re
import functions
import getpass
import encryption

def updateCredentials(file_password):
    SERVER, PORT, USER, PASSWORD = functions.parseCredentials(pwd=file_password)

    print("\n"*5)
    print("Change your credentials", end="\n"*2)
    print("Server [default={}]".format(SERVER))
    server = input("> ")
    server = server or SERVER
    print("Ok")

    print("Port [default={}]".format(PORT))
    port = input("> ")
    port = port or PORT
    print("Ok")

    print("Username [default={}]".format(USER))
    user = input("> ")
    user = user or USER
    print("Ok")

    print("Password (not displayed) [default={}]".format("previous password"))
    password = getpass.getpass("> ")
    password = password or PASSWORD
    print("Ok")

    print("Collecting data...")

    functions.changeCredentials(server=server, port=port, user=user, password=password, pwd=file_password)

    functions.printInGreen("Success")
    print("\n"*5)

    return

def showMails(pwd):
    print("The newest 10 Mails are displayed.")
    print("\n"*5)
    print("Your mails are gonna be displayed now...")
    mails = getMails(pwd=pwd, count=10)

    for mail in mails:
        print("*", mail)
    input("[Press Enter to continue]")
    print("\n"*5)
    return


def sendTUI(pwd):
    print("\n"*5)
    print("Please enter your receiver:")
    receiver = input(">")
    cleaned_receiver = re.match("\S+@\S+.\S+", receiver)
    while not cleaned_receiver:
        functions.printInRed("There was an error while validating your receiver.")
        print("Please enter your receiver again:")
        receiver = input(">")
        cleaned_receiver = re.match("\S+@\S+.\S+", receiver)
    print("Please enter your subject:")
    subject = input(">")

    print("Please enter your message content. If you have finished your text type \"!end!\":")
    text = input(">")
    while True:
        curr = input(">")
        if curr != "!end!":
            text += curr+"\n"
        else:
            break

    send(addr_to=receiver, subject=subject, message=text, password=pwd)

    print("\n"*5)
    return

def start():
    print("Please enter the password for the mail-client:")
    pwd = getpass.getpass("> ")
    working = False
    while not working:
        try:
            encryption.decrypt(pwd)
            working = True
        except:
            functions.printInRed("Your password was not correct. Please try again!")
            pwd = getpass.getpass("> ")
            working = False
    functions.makeMenu()
    select = input("> ")
    while select not in "qQ":
        if select in "sS":
            sendTUI(pwd=pwd)
        elif select in "lL":
            showMails(pwd=pwd)
        elif select in "uU":
            updateCredentials(pwd)
        else:
            functions.printInRed("I can't understand this")
        functions.makeMenu()
        select = input("> ")
    functions.printInBlue("#"*44)
    functions.printInBlue("#{:^42}#".format("Goodbye!"))
    functions.printInBlue("#"*44)

if __name__ == "__main__":
    start()
