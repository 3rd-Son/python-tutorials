book = {}

book['tom'] = {
    'name': 'tom',
    'class': 'js1',
    'phone': 7065903389
}
book['bob'] = {
    'name': 'bob',
    'class': 'js1',
    'phone': 70659033896767
}

import json
s = json.dumps (book) 

with open("/Users/appleplay/Desktop/tutorial/book.txt", 'w') as f:
    f.write(s)