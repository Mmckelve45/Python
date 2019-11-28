#Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.


def collatz(num):
	counter = 0
	while num != 1:
		if num % 2 == 0:
			num = num / 2
			print(num)
			counter += 1
		else:
			num = num * 3 + 1
			print(num)
			counter += 1
	return counter
	print(f"It takes {counter} steps to get to 1")

