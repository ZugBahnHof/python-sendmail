from json.decoder import JSONDecoder
#from email.header import decode_header
from email.header import Header, decode_header, make_header


def parseCredentials(file="secret_credentials.json"):
    jsondec = JSONDecoder()

    text = open(file).read()
    data = jsondec.decode(text)
    print("Opening credential file...")

    return data.get("SERVER", "example.com"), data.get("PORT", 0), data.get("USER", "admin@example.com"), data.get("PASSWORD", "admin")

def parseEmailHeader(subject="=?utf-8?b?U291bmTigJhuIGxpZ2h0?="):
    h = make_header(decode_header(subject))
    return str(h)