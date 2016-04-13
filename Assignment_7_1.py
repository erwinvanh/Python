# import exit-function
# from sys import exit
fname = raw_input("Enter filename: ")
try:
	fhand = open(fname)
except:
    # Print error-message and quit
    print "Enter a valid filename"
    exit(0)	

for line in fhand:
    print line.upper().strip()