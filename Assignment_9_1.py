fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    # Print error-message and quit
    print "Enter a valid filename"
    exit(0) 

# Create empty dictionary
senders = dict()
# Process the file
for line in fh:
    if line.startswith("From "):
        tmpLst = line.split()
        if tmpLst[1] not in senders:
           senders[tmpLst[1]] = 1
        else:
           senders[tmpLst[1]] = senders[tmpLst[1]] + 1

highCount = 0
highSender = ""
for key in senders:
    if senders[key] > highCount:
        highCount = senders[key]
        highSender = key

print highSender, highCount

        
