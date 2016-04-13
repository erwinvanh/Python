# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
# Test
# url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
# Actual assignment
url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Teah.html'
# Get the repeat count
Strcount = raw_input('Enter repeat count : ')
try:
    repeat = int(Strcount)
except:
    exit(0)
# Get the position
Strcount = raw_input('Enter position : ')
try:
    pos = int(Strcount)
except:
    exit(0)

# Functions to open an url and get the tags
def getTags(url):
    html = urllib.urlopen(url).read()
    return BeautifulSoup(html)

# Actual processing
print "Starting with", url
count = 0
while (count < repeat):
    soup = getTags(url)
# Retrieve all of the anchor tags
    tags = soup('a')
# Get the tag at the required position
    url = tags[pos - 1].get('href', None)
    print url
    count += 1
