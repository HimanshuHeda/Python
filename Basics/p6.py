# write a regular program to import a regular statement 
# Write 2 or 3 lines inside a string and use the same command 
# Use all the 4 commands for all the one string only

import re
a = "Welcome To Class"
b = "Jayesh Umre Welcome You"
c = "Welcome to Delhi Capital of. India++"
d = "Jayesh Umre Welcome You"
e = "Good Morning this is Himanshu. Himanshu is in MCA 1st year. Himanshu has completed its BCA from MLSU"


print(re.search("^Welcome.*Class$",a))          # Use to find the text
print(re.findall("e",b))
print(re.findall("w",b))
# print(re.findall("\.",c))
print(re.findall("\+",c))                       # Use to Find 
print(re.split("\s",d))                         # Spliting the text
print(re.sub("Umre","umra",d))

print(re.sub("Himanshu","himanshu",e))
print(re.search("^Himanshu.*Himanshu$",e))
print(re.findall("H",e))
print(re.findall("\.",e))
print(re.split("\s",e))