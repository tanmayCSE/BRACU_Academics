#reading the file
file=open("input.txt","r")
strings=file.readlines()
#print(strings)

#importing the python regex library
import re

#regex for methods
regexMethod="(public|private)*( static|static)?[ (void|int|string|float|double)]+ [a-z][a-zA-Z0-9]+\(((\ )?(\,|\, )*((int|string|float|double)+ [a-zA-Z]+)*)*\)"



#matching lines with the regex and adding matches to the temporary method list
methods=[]
for i in strings:
	if re.search(regexMethod, i)!=None:
		methods.append(re.search(regexMethod, i).group())

print(methods)	


#adding method name to a list
methodName=[]
for i in methods:
	s=i.split("(")
	t=s[0].split(" ")
	methodName.append(t[-1]+"("+s[-1])
print(methodName)


#adding method return type to a list
returnType=[]
regexReturntype="void|int|string|float|double"
for i in methods:
	returnType.append(re.search(regexReturntype, i).group())
print(returnType)


#printing the output
for i in range(len(methods)):
	print(methodName[i]+", Return type: "+returnType[i])
