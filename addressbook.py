import functions


def getAddresses():
    addressBook = open(functions.HOME + "/.sendmail_mailinglist")
    lines = addressBook.read().split("\n")
    addressBook.close()
    addresses = []

    for address in lines:
        if address.startswith("+"):
            addresses.append(address[1:])
    return addresses


def printAddresses(numbering):
    if numbering not in ["numbers", "middle-dot", "minus-sign"]:
        raise ValueError("numbering argument has to bei one of ['numbers', 'middle-dot', 'minus-sign']")

    lines = getAddresses()

    if numbering == "numbers":
        for number, line in enumerate(lines):
            print(number, ": ", line, sep="")

        return number

    else:
        if numbering == "minus-sign":
            numbering = "- "
        else:
            numbering = "· "
        for line in lines:
            print(numbering, line, sep="")
    return True


def removeAddress(i: int):
    addresses = getAddresses()
    tmp_addresses = ["+" + addresses[i]]

    new_addresses = set(addresses) - set(tmp_addresses)

    addressBook = open(functions.HOME + "/.sendmail_mailinglist", "w")
    for address in new_addresses:
        addressBook.write("{addr}\n".format(addr=address))
    addressBook.close()

    return True


def addAddress(address):
    addressBook = open(functions.HOME + "/.sendmail_mailinglist", "a")
    addressBook.write("+{addr}\n".format(addr=address))
    addressBook.close()

    return True
