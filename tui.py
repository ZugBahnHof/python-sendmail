# Not a real TUI, just a bunch of prints and inputs
from sendmail import send
from receivemail import getMails
import re
import functions
import getpass
import encryption
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

default_style = Style.from_dict({
    'rprompt': 'bg:#fff #000',
})

def updateCredentials(file_password):
    SERVER, PORT, USER, PASSWORD = functions.parseCredentials(pwd=file_password)

    print("\n"*5)
    print("Change your credentials", end="\n"*2)
    print("Server")
    server = prompt('> ', rprompt="[default={}]".format(SERVER), style=default_style)
    server = server or SERVER
    print("Ok")

    print("Port")
    port = prompt('> ', rprompt="[default={}]".format(PORT), style=default_style)
    port = port or PORT
    print("Ok")

    print("Username")
    user = prompt('> ', rprompt="[default={}]".format(USER), style=default_style)
    user = user or USER
    print("Ok")

    print("Password [default={}]".format("previous password"))
    password = prompt("> ", is_password=True)
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
    receiver = prompt("> ", validator=functions.validateEmail())
    print("Please enter your subject:")
    subject = input("> ")

    print("Please enter your message content. If you have finished your text press ALT + ENTER:")

    text = prompt('> ', multiline=True,
           prompt_continuation=functions.prompt_continuation)

    send(addr_to=receiver, subject=subject, message=text, password=pwd)

    print("\n"*5)
    return

def start():
    print("Please enter the password for the mail-client:")
    pwd = prompt("> ", is_password=True)
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
