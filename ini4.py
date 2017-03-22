# print the odd numbers in the (a, b) range

a = 4840 # lower term in the range
b = 9372 # upper term in the range
total = 0
for i in range(a, b): 
	if(i % 2 != 0): # if the result of dividing i by 2 is not zero
		total += i
print(total)
