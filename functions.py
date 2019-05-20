from json.decoder import JSONDecoder
from json.encoder import JSONEncoder
#from email.header import decode_header
from email.header import Header, decode_header, make_header


def parseCredentials(file="secret_credentials.json"):
    jsondec = JSONDecoder()

    text = open(file).read()
    data = jsondec.decode(text)
    print("Opening credential file...")

    return data.get("SERVER", "example.com"), data.get("PORT", 0), data.get("USER", "admin@example.com"), data.get("PASSWORD", "admin")

def changeCredentials(server, port, user, password, file="secret_credentials.json"):
    jsonenc = JSONEncoder()

    data = {
        "SERVER": server,
        "PORT": port,
        "USER": user,
        "PASSWORD": password
    }

    json = jsonenc.encode(data)

    print("Opening credential file...")
    f = open(file)
    f.write(json)

    print("Saving...")

    return

def parseEmailHeader(subject="=?utf-8?b?U291bmTigJhuIGxpZ2h0?="):
    h = make_header(decode_header(subject))
    return str(h)

def deletSpaces(string=""):
    return " ".join(string.split())

def makeMenu():
    print("|", "⎺" * 42, "|", sep="")
    print("|", "{:^40}".format("Welcome to this commandline mailclient!"), "|")
    print("|", "–" * 42, "|", sep="")
    print("|{:<42}|".format("Choose your option:"))
    print("|{:<20}".format("[S]end a mail"), "{:>20}|".format("[L]ist 10 newest mails"), sep="")
    print("|{:<42}|".format("[Q]uit"))
    print("|", "_" * 42, "|", sep="")
    return