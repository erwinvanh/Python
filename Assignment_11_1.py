import re
# Actual file (assignment) - There are 65 values and the sum ends with 571
name = "regex_sum_229799.txt"
# File for testing - There are 116 values with a sum=597873
# name = "regex_sum_42.txt"
handle = open(name)

numsum = 0
numcount = 0
for line in handle:
    numlist = re.findall('[0-9]+', line)
    if len(numlist) > 0:
        for number in numlist:
            numsum = numsum + int(number)
            numcount = numcount + 1

print "Sum is" , numsum
print "Number of integers is", numcount
