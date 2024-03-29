#!/usr/bin/python3
# Not a real TUI, just a bunch of prints and inputs
from sendmail import send
from receivemail import getMails
import addressbook as ab
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
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion.filesystem import PathCompleter

# SQLCompleter = WordCompleter(['select', 'from', 'insert', 'update', 'delete', 'drop'],
#                              ignore_case=True)


default_style = Style.from_dict({
    'rprompt': 'bg:#fff #000',
})
style = Style.from_dict({
    "wbg": "bg:#fff #000",
})


def updateCredentials(file_password):
    SERVER, PORT, USER, PASSWORD = functions.parseCredentials(pwd=file_password)

    os.system('clear')
    print("Change your credentials", end="\n" * 2)
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


def addressBookTUI():
    os.system("clear")
    print("This is your address book:")
    ab.printAddresses("middle-dot")

    print("Do you want to [d]elete an address, [a]dd another one, or do nothing (write something else)?")
    selection = prompt("> ")

    if selection == "":
        return

    elif selection in "dD":
        print("Which address do you want to delete?")

        count = ab.printAddresses("numbers")

        deleter = prompt("> ", validator=functions.validateNumberUnderX(X=count))
        ab.removeAddress(int(deleter))

    elif selection in "aA":
        print("Type in the address to add:")
        addr_to_add = prompt("> ", validator=functions.validateEmail())

        ab.addAddress(addr_to_add)

    os.system("clear")
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

    session = PromptSession(history=FileHistory(functions.HOME + '/.sendmail_mailinglist'))

    print_formatted_text(HTML('Please enter your receiver (if you get suggested adresses, just press <wbg>→ </wbg>:'),
                         style=style)
    receiver = session.prompt("> ", validator=functions.validateEmail(), auto_suggest=AutoSuggestFromHistory())
    print("Please enter your subject:")
    subject = input("> ")
    print_formatted_text(HTML(
        'Please enter your message content. If you have finished your text press <wbg>ALT</wbg> + <wbg>ENTER</wbg>:'),
                         style=style)
    print("")

    text = prompt('> ', multiline=True,
                  prompt_continuation=functions.prompt_continuation, mouse_support=True)
    attachment = confirm("Do you want to add one attachment to the email?")
    if attachment:
        print_formatted_text(HTML(
            "Please enter the whole filepath to your attachment file. For example: <ansigreen>/home/lolo/documents/test.pdf</ansigreen>"))
        filepath = prompt("> ", validator=functions.validateFilePath(), completer=PathCompleter())
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
            os.system('clear')
        elif select in "lL":
            showMails(pwd=pwd)
            os.system('clear')
        elif select in "uU":
            updateCredentials(pwd)
            os.system('clear')
        elif select in "rR":
            rainbow.main()
            os.system('clear')
        elif select in "aA":
            addressBookTUI()
            os.system('clear')
        else:
            functions.printInRed("I can't understand this")
        TERMINAL_SIZE = gts.get_terminal_size()[0]
        functions.makeMenu(TERMINAL_SIZE=TERMINAL_SIZE)
        select = input("> ")
    os.system('clear')
    functions.printInBlue("#" * TERMINAL_SIZE)
    functions.printInBlue("#{0:^{1}}#".format("Goodbye!", TERMINAL_SIZE - 2))
    functions.printInBlue("#" * TERMINAL_SIZE)


if __name__ == "__main__":
    start()
