from json.decoder import JSONDecoder
def parseCredentials(file="secret_credentials.json"):
    jsondec = JSONDecoder()

    text = open(file).read()
    data = jsondec.decode(text)
    print("Opening credential file...")

    return data.get("SERVER", "example.com"), data.get("PORT", 0), data.get("USER", "admin@example.com"), data.get("PASSWORD", "admin")