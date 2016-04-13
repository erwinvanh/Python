fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
    # Print error-message and quit
    print "Enter a valid filename"
    exit(0)	

lst = list()
for line in fh:
    tmpLst = line.split()
    for word in tmpLst:
        if word in lst:
           continue
        else:
            lst.append(word)
lst.sort()
print lst