# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

# url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_229804.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
spanSum  = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    spanSum = spanSum + int(tag.contents[0])

print spanSum
