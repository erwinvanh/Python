# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
    # Print error-message and quit
    print "Enter a valid filename"
    exit(0)	
numSpamLines = 0.0
spamConfidence = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
	# Process this line
    numSpamLines = numSpamLines + 1.0
    start = line.find('0.')
    xspamConfidence = line[start:]
    spamConfidence = spamConfidence + float(xspamConfidence)
	
#print "Lines " ,numSpamLines
#print "spamConfidence" , spamConfidence
print "Average spam confidence:" , (spamConfidence / numSpamLines)