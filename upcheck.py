#!/usr/bin/env python3

# Kudos to Reuven from LinuxJournal for the backbone: https://www.linuxjournal.com/content/threading-python

import sys
import requests
import threading
from queue import Queue

urls = ["https://%s"%line.strip('\n') for line in open(sys.argv[1],'r')]

queue = Queue()
threads = []

def get_length(url):
	try:
		response = requests.get(url)
		queue.put((url, str(response.status_code)))

	except requests.packages.urllib3.exceptions.LocationValueError as ee:
		queue.put("Location value error for "+url)

	except requests.exceptions.SSLError as eee:
		queue.put("SSL error, please verify this manually "+url)

	except requests.exceptions.ConnectionError as e:
		queue.put("Could not connect to "+url)

	except Exception as eeee:
		print(eeee.message)

print("There are %s"%len(urls)+" urls to be checked...")

for url in urls:
	t = threading.Thread(target=get_length, args=(url,))
	threads.append(t)
	t.start()

for one_thread in threads:
	one_thread.join()

while not queue.empty():
	url = queue.get()
	if "Could not connect" not in url:
		print(url)
