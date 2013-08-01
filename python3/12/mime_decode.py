#!/usr/bin/env python3
# Foundations of Python Network Programming - Chapter 12 - mime_decode.py

import email, fileinput, sys

def save_parts(message, level=0, counter=1):
    l = "|  " * level
    if message.is_multipart():
        print(l + "Found multipart:")
        for item in message.get_payload():
            counter = save_parts(item, level + 1, counter)
    else:
        filename = 'part{}.out'.format(counter)
        print('Part {}:'.format(counter),
              message.get('content-type', '-'),
              message.get('content-disposition', '-'),
              '=>', filename)
        with open(filename, 'wb') as f:
            f.write(message.get_payload(decode=1))
        counter += 1
    return counter

with open(sys.argv[1]) as f:
    message = email.message_from_string(''.join(fileinput.input()))
save_parts(message)
