# Based on https://gist.github.com/yehgdotnet/b9dfc618108d2f05845c4d8e28c5fc6a. Kudos for inspiration!

import mmh3
import requests
import codecs
import sys

response = requests.get(sys.argv[1],verify=False)
favicon = codecs.encode(response.content, 'base64')
hash = mmh3.hash(favicon)
print('\nShodan search query: http.favicon.hash:'+str(hash))

