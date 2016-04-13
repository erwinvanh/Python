import sqlite3
import time
import urllib
import zlib

conn = sqlite3.connect('index.sqlite')
conn.text_factory = str
cur = conn.cursor()

# Determine the top ten organizations
cur.execute('''SELECT Messages.id, sender FROM Messages
    JOIN Senders ON Messages.sender_id = Senders.id''')

sendorgs = dict()
for message_row in cur :
    sender = message_row[1]
    pieces = sender.split("@")
    if len(pieces) != 2 : continue
    dns = pieces[1]
    sendorgs[dns] = sendorgs.get(dns,0) + 1

# pick the top schools
orgs = sorted(sendorgs, key=sendorgs.get, reverse=True)
orgs = orgs[:10]
print "Top 10 Organizations"
print orgs
# orgs = ['total'] + orgs

# Read through the messages
counts = dict()
period = list()

cur.execute('''SELECT Messages.id, sender, sent_at FROM Messages
    JOIN Senders ON Messages.sender_id = Senders.id''')

for message_row in cur :
    sender = message_row[1]
    pieces = sender.split("@")
    if len(pieces) != 2 : continue
    dns = pieces[1]
    if dns not in orgs : continue
    # Count by month
    period = message_row[2][:7]
    if period not in periods : periods.append(period)
    key = (period, dns)
    counts[key] = counts.get(key,0) + 1
    tkey = (period, 'total')
    counts[tkey] = counts.get(tkey,0) + 1

periods.sort()
print counts
print periods


fhand = open('gline.js','w')
#fhand.write("gline = [ ['Month'")
fhand.write("gline = [ ['Year'")
for org in orgs:
    fhand.write(",'"+org+"'")
fhand.write("]")

# for month in months[1:-1]:
for period in periods:
    fhand.write(",\n['"+period+"'")
    for org in orgs:
        key = (period, org)
        val = counts.get(key,0)
        fhand.write(","+str(val))
    fhand.write("]");

print "Data written to gline.js"
print "Open gline.htm in a browser to view"
