# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number

#1,1,2,3,5,8,13,21
def fibonacci(n):
	if n >= 3:
		return Fibonacci(n-2)+Fibonacci(n-1)
	else:
		return 1

