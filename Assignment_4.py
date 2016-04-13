def computepay(h,r):
    if h <= 40:
        pay = h * r
    else:
        pay = (40 * r) + (h - 40) * 1.5 * r
    return pay

str_hrs = raw_input("Enter Hours:")
str_rate = raw_input("Enter rate:")
try:
    i_hrs = float(str_hrs)
    i_rate = float(str_rate)
except:
    print "Input is invalid" 
    i_hrs = 0

if i_hrs > 0:
    p = computepay(i_hrs, i_rate)
    print "Pay",p