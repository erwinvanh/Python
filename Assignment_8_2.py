fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
	fh = open(fname)
except:
    # Print error-message and quit
    print "Enter a valid filename"
    exit(0)	

count = 0
for line in fh:
    if line.startswith("From "):
        tmpLst = line.split()
        print tmpLst[1]
        count = count + 1
	    
print "There were", count, "lines in the file with From as the first word"
