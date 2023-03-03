f = open('/Users/appleplay/Desktop/tutorial/book.txt', 'r')
s = f.read()
print(s)

import json
book = json.loads(s)
print(book)

type(book)