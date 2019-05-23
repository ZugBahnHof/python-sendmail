import tui
import encryption
import functions
import os
import getpass

try: os.remove("data.aes")
except: pass

print("Choose your password for this mailclient [default=asdf]")
functions.printInRed("Warning! This password can't be changed!")

password_for_mailclient = getpass.getpass("> ")
while len(password_for_mailclient) < 5:
    functions.printInRed("Please give a password that is longer than 5 characters!")
    password_for_mailclient = getpass.getpass("> ")

encryption.encrypt("{}", password_for_mailclient)

tui.updateCredentials(file_password=password_for_mailclient)

functions.printInBlue("#"*44)
functions.printInBlue("#{:^42}#".format("You can now start your mail-client!"))
functions.printInBlue("#"*44)