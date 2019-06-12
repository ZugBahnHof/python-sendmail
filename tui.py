#!/usr/bin/python3
# Not a real TUI, just a bunch of prints and inputs
from sendmail import send
from receivemail import getMails
import os
import functions
import getpass
import encryption
from prompt_toolkit import prompt, print_formatted_text, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog, confirm
import rainbow
import sys
import getTerminalSize as gts


default_style = Style.from_dict({
    'rprompt': 'bg:#fff #000',
})
style = Style.from_dict({
    "wbg": "bg:#fff #000",
})

def updateCredentials(file_password):
    SERVER, PORT, USER, PASSWORD = functions.parseCredentials(pwd=file_password)

    os.system('clear')
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
    os.system('clear')

    return

def showMails(pwd):
    print("The newest 10 Mails are displayed.")
    os.system('clear')
    print("Your mails are gonna be displayed now...")
    mails = getMails(pwd=pwd, count=10)

    for mail in mails:
        print("*", mail)
    input("[Press Enter to continue]")
    os.system('clear')
    return


def sendTUI(pwd):
    os.system('clear')
    print("Please enter your receiver:")
    receiver = prompt("> ", validator=functions.validateEmail())
    print("Please enter your subject:")
    subject = input("> ")
    print_formatted_text(HTML('Please enter your message content. If you have finished your text press <wbg>ALT</wbg> + <wbg>ENTER</wbg>:'), style=style)
    print("")

    text = prompt('> ', multiline=True,
           prompt_continuation=functions.prompt_continuation, mouse_support=True)
    attachment = confirm("Do you want to add one attachment to the email?")
    if attachment:
        print_formatted_text(HTML("Please enter the whole filepath to your attachment file. For example: <ansigreen>/home/lolo/documents/test.pdf</ansigreen>"))
        filepath = prompt("> ", validator=functions.validateFilePath())
    else:
        filepath = None

    send(addr_to=receiver, subject=subject, message=text, password=pwd, filename=filepath)

    os.system('clear')
    return

def start():
    TERMINAL_SIZE = gts.get_terminal_size()[0]
    pwd = input_dialog(title='LOGIN', text='Please enter the password for the mail-client:', password=True)
    working = False
    if not pwd or len(pwd) <= 1:
        sys.exit()
    while not working:
        try:
            encryption.decrypt(pwd)
            working = True
        except:
            pwd = input_dialog(title='LOGIN', text='Your password was incorrect! Please try again:', password=True)
            working = False
            if not pwd or len(pwd) <= 1:
                sys.exit()
    os.system('clear')
    functions.makeMenu(TERMINAL_SIZE=TERMINAL_SIZE)
    select = input("> ")
    while select not in "qQ":
        if select in "sS":
            sendTUI(pwd=pwd)
        elif select in "lL":
            showMails(pwd=pwd)
        elif select in "uU":
            updateCredentials(pwd)
        elif select in "rR":
            rainbow.main()
        else:
            functions.printInRed("I can't understand this")
        TERMINAL_SIZE = gts.get_terminal_size()[0]
        functions.makeMenu(TERMINAL_SIZE=TERMINAL_SIZE)
        select = input("> ")
    os.system('clear')
    functions.printInBlue("#"*TERMINAL_SIZE)
    functions.printInBlue("#{0:^{1}}#".format("Goodbye!", TERMINAL_SIZE-2))
    functions.printInBlue("#"*TERMINAL_SIZE)

if __name__ == "__main__":
    start()
