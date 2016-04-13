import re
line = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'

numlist = re.findall('href="(.+)"', line)
print numlist

numlist = re.findall('href=".+"', line)
print numlist

numlist = re.findall('http://.*', line)
print numlist

numlist = re.findall('<.*>', line)
print numlist
