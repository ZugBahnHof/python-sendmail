# Not a real TUI, just a bunch of prints and inputs
from sendmail import send
import re

def start():
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

if __name__ == "__main__":
    start()
