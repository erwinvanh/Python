largest = None
smallest = None
while True:
    str_num = raw_input("Enter a number: ")
    if str_num == "done" : break
    try:
        num = int(str_num)
        if largest is None:
            largest = num
        elif num > largest:
            largest = num
        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
        
    except:
        print "Invalid input" 

print "Maximum is", largest
print "Minimum is", smallest