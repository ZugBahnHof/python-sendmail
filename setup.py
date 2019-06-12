import tui
import encryption
import functions
import os
import getpass
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator

def valiPass(text):
    return len(text) > 5

validator = Validator.from_callable(
    valiPass,
    error_message='Please enter at least 6 characters',
    move_cursor_to_end=True)

try: os.remove("data.aes")
except: pass

f = open(functions.HOME + "/.sendmail_mailinglist", "w")
f.close()

print("Choose your password for this mailclient")
functions.printInRed("Warning! This password can't be changed!")

password_for_mailclient = prompt("> ", is_password=True, validator=validator)

encryption.encrypt("{}", password_for_mailclient)

tui.updateCredentials(file_password=password_for_mailclient)

functions.printInBlue("#"*44)
functions.printInBlue("#{:^42}#".format("You can now start your mail-client!"))
functions.printInBlue("#"*44)