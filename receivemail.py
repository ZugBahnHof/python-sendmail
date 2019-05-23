import imaplib
import functions
import re

def getMails(count=20, pwd):
    SERVER, PORT, USER, PASSWORD = functions.parseCredentials(pwd=pwd)

    # connect to host using SSL
    imap = imaplib.IMAP4_SSL(SERVER)

    ## login to server
    imap.login(USER, PASSWORD)

    imap.select('Inbox')

    tmp, data = imap.search(None, 'ALL')

    sub = re.compile("Subject:.*")

    c = 0

    mails = []

    for num in reversed(data[0].split()):
        tmp, data = imap.fetch(num, '(RFC822)')
        #print('Message: {0}\n'.format(num))
        context = data[0][1].decode("utf-8")
        tmp_sub = sub.findall(context)

        #print(context)

        if tmp_sub != []:
            tmp_sub = tmp_sub[-1][8:]
            #print(tmp_sub)
            mails.append(functions.deletSpaces(functions.parseEmailHeader(tmp_sub)))

            c += 1

        if c >= count:
            break
        #print(data[0][1])
    imap.close()

    return mails
