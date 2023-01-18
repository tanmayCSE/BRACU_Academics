import re

regex = []
reg_count = int(input("Number of inputs for regex: "))
for i in range(0,reg_count):
	sol1 = re.compile(input())

	regex.append(sol1)

string = []
string_count = int(input("Number of inputs for string: "))
for i in range(0,string_count):
	sol2 = input()

	string.append(sol2)

for i in range(len(string)):
	not_matched = 0
	for j in range(len(regex)):
		if(regex[j].match(string[i])):
			print(f"YES, {j+1}")
			break
		else:
			not_matched += 1
	if(not_matched == reg_count):
			print(f"NO, 0")