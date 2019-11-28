#Factorial

if n >= 1:
	n! = n * (n-1)!
elif n=0:
	return 1


#recursive because it calls itself
def fact(n):
	if n >= 1:
		return n * fact(n-1)
	else:
		return 1

#Fibonacci Sequence 1,1,2,3,5,8 adds the previous two numbers to get next number
#n is the number in the sequence (nth number of the sequence)
#Fn = Fn-1 + Fn-2


def fib(n):
	if n >= 3: #recursive case
		return fib(n-2)+ fib(n-1)
	else: #base case
		return 1