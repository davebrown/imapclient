# Copyright (c) 2014, Menno Smits
# Released subject to the New BSD License
# Please see http://en.wikipedia.org/wiki/BSD_licenses

from imapclient import IMAPClient

HOST = 'imap.host.com'
USERNAME = 'someuser'
PASSWORD = 'secret'

server = IMAPClient(HOST)
server.login(USERNAME, PASSWORD)

select_info = server.select_folder('INBOX')
print('%d messages in INBOX' % select_info[b'EXISTS'])

messages = server.search(['NOT', 'DELETED'])
print("%d messages that aren't deleted\n" % len(messages))

print("Messages:")
response = server.fetch(messages, ['FLAGS', 'RFC822.SIZE'])
for msgid, data in response.items():
    print('   ID %d: %d bytes, flags=%s' % (msgid,
                                            data[b'RFC822.SIZE'],
                                            data[b'FLAGS']))

server.logout()
