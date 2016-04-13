# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
import httplib
import urllib
from urllib import FancyURLopener
from BeautifulSoup import *

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
httplib.HTTPConnection.debuglevel = 1
urlopen = MyOpener().open
urlretrieve = MyOpener().retrieve

series = "blacklist"
url = 'http://www.addic7ed.com/search.php?search=' + series + '&Submit=Search'
try:
    handle = urllib.urlopen(url)
    html = handle.read()
    if len(html) == 0:
        print "No data received"
        print handle.getcode()
        exit(0)
except:
    print "Error opening URL"
    exit(0)

handle.close()

soup = BeautifulSoup(html)
tags = soup('a')
for tag in tags:
    for content in tag.contents:
        name = str(content)
        if series.upper() in name.upper():
            print content
            print tag.get('href', None)
            href = tag.get('href', None)

# Suffix /1 means english

url = "http://www.addic7ed.com/" + href
print "Get subs for " , url

html = urllib.urlopen(url).read()
if len(html) == 0:
    print "No data received"
    exit(0)

soup = BeautifulSoup(html)
copy = open("soup.txt", "w")
copy.write(url)
tags = soup('div' , {"id": "container95m"})
tagcount = 0
for tag in tags:
    tagcount += 1
    souptag = BeautifulSoup(str(tag))
    tds = souptag('td')
    tdcount = 0
    for td in tds:
        tdcount += 1
        line = str(tagcount) + ":" + str(tdcount) + " " + str(td)
        copy.write(str(line))
        copy.write('\n')

copy.close()
