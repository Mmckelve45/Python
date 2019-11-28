#Program that finds the prime numbers until the user chooses to stop asking for the next one.



num = int(input("Please enter an integer > 2: "))


def find_prime(num):
	for i in range(1,num):
			if (num % i) == 0:
				return False
	return True








num += 1
while find_prime(num) == False:
	num += 1
print(f"{num} is your next prime")


	#next_prime = input("Would you like to see the next prime number? Enter Yes or No: ")
	#while next_prime.lower()[0] == 'y':
					#next_prime = input("Would you like to see the next prime number? Enter Yes or No: ")
