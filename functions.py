from json.decoder import JSONDecoder
def parseCredentials(file="secret_credentials.json"):
    jsondec = JSONDecoder()

    text = open(file).read()
    data = jsondec.decode(text)

    return data.get("SERVER", None), data.get("PORT", 0), data.get("USER", "admin"), data.get("PASSWORD", "admin")