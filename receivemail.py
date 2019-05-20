import imaplib
import pprint
import functions
import re

SERVER, PORT, USER, PASSWORD = functions.parseCredentials()

# connect to host using SSL
imap = imaplib.IMAP4_SSL(SERVER)

## login to server
imap.login(USER, PASSWORD)

imap.select('Inbox')

tmp, data = imap.search(None, 'ALL')

sub = re.compile("Subject:.*")

c = 0

for num in reversed(data[0].split()):
    tmp, data = imap.fetch(num, '(RFC822)')
    #print('Message: {0}\n'.format(num))
    context = data[0][1].decode("utf-8")
    tmp_sub = sub.findall(context)

    #print(context)

    if tmp_sub != []:
        tmp_sub = tmp_sub[0][8:]
        #print(tmp_sub)
        print(functions.parseEmailHeader(tmp_sub))

        c += 1

    if c == 20:
        break
    #print(data[0][1])
imap.close()
