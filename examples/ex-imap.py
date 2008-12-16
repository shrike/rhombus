#!/usr/bin/env python
from imaplib import *

# fill these in if you want to connect
user = ""
passwd = ""

server = IMAP4_SSL ("imap.gmail.com")
server.login (user, passwd)
server.select ()
typ, data = server.search (None, 'ALL')

# num is which email to read. 
# 2 for me means second from the bottom (nd oldest)
num = 2
typ, data = server.fetch (num, '(RFC822)')
print (data[0][1])

server.close()
server.logout()

print ("Done.")
