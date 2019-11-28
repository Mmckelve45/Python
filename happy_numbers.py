#starting with positive integer, replace the number by the sum of the squares of its digits


def sumSquares(num):
	sum = 0
	digits = str(num)
	
	while sum != 1:

		for i in range(0,len(digits)):
			print(int(digits[i]))
			sum += int(digits[i]) ** 2
			print("\n")













def sumSquares(num):
	sum = 0
	digits = str(num)
	for i in range(0,len(digits)):
		print(int(digits[i]))
		sum += int(digits[i]) ** 2
	return sum