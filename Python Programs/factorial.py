n = int(input("Enter the limit:"))
fact = 1
if (n == 0):
	print("Factorial is 1")
elif (n < 0):
	print("Can't find the factorial")
else:
	for i in range(1,n+1):
		fact = fact * i
	print("The factorial of",n,"is ",fact)