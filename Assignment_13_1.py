import urllib
import xml.etree.ElementTree as ET
# URL For testing
# url = 'http://python-data.dr-chuck.net/comments_42.xml'
url = 'http://python-data.dr-chuck.net/comments_229801.xml'

uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)

totalcount = 0
occurs = 0
counts = tree.findall('.//count')
for counttag in counts:
    totalcount += int(counttag.text)
    occurs += 1

print "Total is", totalcount
print "Occurs is", occurs
