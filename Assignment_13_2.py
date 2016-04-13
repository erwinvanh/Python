import urllib
import json

while True:
    url = raw_input('Enter url: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    info = json.loads(data)

    total = 0
    comments = info['comments']
    for item in comments:
        print 'Count', item['count']
        total +=  int(item['count'])

    print "Total is", total
