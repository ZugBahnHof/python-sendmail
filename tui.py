# Not a real TUI, just a bunch of prints and inputs
from sendmail import send
from receivemail import getMails
import re

def showMails():
    print("The newest 10 Mails are displayed.")
    print("\n"*5)
    print("Your mails are gonna be displayed now...")
    mails = getMails(10)

    for mail in mails:
        print(mail)
    return


def sendTUI():
    print("Welcome to this commandline mailclient!", end="\n\n")
    print("Please enter your receiver:")
    receiver = input(">")
    cleaned_receiver = re.match("\S+@\S+.\S+", receiver)
    while not cleaned_receiver:
        print("There was an error while validating your receiver. Please enter your receiver again:")
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

    send(addr_to=receiver, subject=subject, message=text)

    return

def start():
    print("|", "⎺"*42, "|", sep="")
    print("|", "{:^40}".format("Welcome to this commandline mailclient!"), "|")
    print("|", "–" * 42, "|", sep="")
    print("|{:<42}|".format("Choose your option:"))
    print("|{:<20}".format("[S]end a mail"), "{:>20}|".format("[L]ist 10 newest mails"), sep="")
    print("|{:<42}|".format("[Q]uit"))
    print("|", "_" * 42, "|", sep="")
    select = input("> ")
    while select:
        if select in "sS":
            sendTUI()
        elif select in "lL":
            showMails()
        elif select in "qQ":
            break
        else:
            print("I can't understand this")
        select = input("> ")
    print("#"*44)
    print("#{:^42}#".format("Goodbye!"))
    print("#"*44)

if __name__ == "__main__":
    start()
