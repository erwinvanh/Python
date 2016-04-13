name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hourdict = dict()
for line in handle:
    if line.startswith("From "):
        tmpLst = line.split()
        time = tmpLst[5]
        tmpLst = time.split(":")
        hour = tmpLst[0]
        if hour not in hourdict:
            hourdict[hour] = 1
        else:
            hourdict[hour] = hourdict[hour] + 1

hourlist = list()
for key, val in hourdict.items():
    hourlist.append( (key, val) )

hourlist.sort()

for key, val in hourlist:
    print key, val
                    