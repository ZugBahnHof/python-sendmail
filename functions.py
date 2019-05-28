from json.decoder import JSONDecoder
from json.encoder import JSONEncoder
from email.header import decode_header, make_header
from prompt_toolkit import print_formatted_text, HTML, prompt
from prompt_toolkit.validation import Validator, ValidationError
import encryption
import re

def parseCredentials(pwd, file="secret_credentials.json"):
    jsondec = JSONDecoder()

    text = encryption.decrypt(password=pwd) or "{}"
    data = jsondec.decode(text)
    print("Opening credential file...")

    return data.get("SERVER", "example.com"), data.get("PORT", "0"), data.get("USER", "admin@example.com"), data.get("PASSWORD", "admin")

def changeCredentials(server, port, user, password, pwd, file="secret_credentials.json"):
    jsonenc = JSONEncoder()

    data = {
        "SERVER": server,
        "PORT": port,
        "USER": user,
        "PASSWORD": password
    }

    json = jsonenc.encode(data)

    print("Opening credential file...")
    encryption.encrypt(text=json, password=pwd)
    print("Saving...")

    return

def parseEmailHeader(subject="=?utf-8?b?U291bmTigJhuIGxpZ2h0?="):
    h = make_header(decode_header(subject))
    return str(h)

def deletSpaces(string=""):
    return " ".join(string.split())

def makeMenu(TERMINAL_SIZE):
    if type(TERMINAL_SIZE) is not int:
        raise AttributeError("TERMINAL_SIZE has to be an integer")
    print("|", "⎺" * (TERMINAL_SIZE-2), "|", sep="")
    print("|", "{0:^{1}}".format("Welcome to this commandline mailclient!", (TERMINAL_SIZE-2)), "|", sep="")
    print("|", "–" * (TERMINAL_SIZE-2), "|", sep="")
    print("|{0:<{1}}|".format("Choose your option:", TERMINAL_SIZE-2))
    halfSize = int((TERMINAL_SIZE-2)/2)
    if TERMINAL_SIZE % 2 == 1:
        halfSize2 = halfSize + 1
    else:
        halfSize2 = halfSize
    print("|{0:<{1}}{2:<{3}}|".format("[S]end a mail 📨", halfSize, "[L]ist 10 newest mails 🗒️", halfSize2), sep="")
    print("|{0:<{1}}{2:<{3}}|".format("[U]pdate credentials 🔐", halfSize, "[Q]uit 📴", halfSize2-2), sep="")
    print("|", "_" * (TERMINAL_SIZE-2), "|", sep="")
    return

def printInGreen(text=""):
    print_formatted_text(HTML('<ansigreen>{text}</ansigreen>'.format(text=text)))

def printInRed(text=""):
    print_formatted_text(HTML('<ansired>{text}</ansired>'.format(text=text)))

def printInBlue(text=""):
    print_formatted_text(HTML("<skyblue>{text}</skyblue>".format(text=text)))

def prompt_continuation(width, line_number, is_soft_wrap):
    return '> '

class validateEmail(Validator):
    def validate(self, document):
        text = document.text

        validation = re.match("\S+@\S+\.\S+", text)

        if not validation:
            raise ValidationError(message="This is not a valid E-Mail adress")