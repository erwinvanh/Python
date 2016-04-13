# import exit-function
from sys import exit
fname = raw_input("Enter filename: ")
try:
	fhand = open(fname)
	print "Success" 
except:
    # Print error-message and quit
    print "Enter a valid filename"
    exit(0)	

copy = open("copy.txt", "w")	
count = 0
countfrom = 0
for line in fhand:
    count =  count + 1
    if line.startswith("From:") :
        #print line.rstrip()
        copy.write(line)
        countfrom = countfrom + 1

copy.close()
print "Line-count : ", count
print "Lines starting with From ", countfrom
	
