import os
import pyAesCrypt

def encrypt(text, password):
    bufferSize = 64 * 1024
    # write text to a temp file
    file = open("data.txt", "w")
    file.write(text)
    file.close()
    # encrypt
    pyAesCrypt.encryptFile("data.txt", "data.aes", password, bufferSize)
    # delete temp file
    os.remove("data.txt")

    return

def decrypt(password):
    bufferSize = 64 * 1024
    # decrypt file
    pyAesCrypt.decryptFile("data.aes", "dataout.txt", password, bufferSize)
    # read text to a temp file
    file = open("dataout.txt", "r")
    text = file.read()
    file.close()
    # delete temp file
    os.remove("dataout.txt")

    return text