#LESSER OF TWO EVENS: 
#Write a function that returns the lesser of two given
#numbers if both numbers are even, but returns the 
#greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
	if a % 2 ==0 and b % 2 == 0:
		return min(a,b)
	else:
		return max(a,b)

#function that takes in 2 word string and returns True if both words begin with the same letter
def animal_crackers(text):
	x = text.lower().split()
	return x[0][0] == x[1][0]
	

#Makes Twenty
#given two ints, return true if the sum of the integers is 20 or if one of the ints is 20
#if not, return false

def makes_twenty(a,b):
	sum = a + b
	return sum == 20 or a == 20 or b == 20

#-----------------Level 1 problems-----------------------#
#function that capitalizes the first and fourth letter of a name
def capital(name):
	first_letter = name[0]
	inbetween = name[1:3]
	fourth_letter = name[3]
	rest = name[4:]
	return first_letter.upper() + inbetween + fourth_letter.upper() + rest

def capital(name):
	first_half = name[:3]
	second_half = name[3:]
	return first_half.capitalize() + second_half.capitalize()


#Given a sentence, return a sentence with the words reversed
#use .join() method here?
mylist = ['a','b','c']
'--'.join(mylist)
#returns 'a--b--c'

def yoda(text):
	wordlist = text.split()
	reverse_word_list = wordlist[::-1]
	return ' '.join(reverse_word_list)



#given an int, return true if num is within 10 of either 100 or 200
def almost_there(num):
	if num <= 110 and num >= 90 or num <= 210 and num >= 190:
		return True
	else:
		return False

def almost_there(n):
	return (abs(100-n) <= 10) or (abs(200-n) <= 10)


#def has_33(nums):
#	x = 0
#	for i in nums:
#		if nums[x] == nums[x+1] and nums[x] == 3:
#			return True
#		else:
#			return False
#		x+=1

def has_33(nums):
	for i in range(0,len(nums)-1):
		if nums[i] == 3 and nums[i+1] == 3:
			return True
	return False

#given a string, return a string where for every character in the original there are 3 chars
def paper_doll(text):
	result = ''
	for char in text:
		result += char*3
	return result


#Given three integers between 1 and 11, if their sum is less than or equal to 21, 
#return their sum. If their sum exceeds 21 and there's an eleven, 
#reduce the total sum by 10. Finally, 
#if the sum (even after adjustment) exceeds 21, return 'BUST

def blackjack(a,b,c):
	add3 = a + b + c 
	if add3 > 21 and a == 11 or b == 11 or c == 11:
		return add3 - 10
	elif add3 < 22:
		return add3
	else:
		return "BUST"

def blackjack(a,b,c):
	if sum([a,b,c]) <= 21:
		return sum([a,b,c])
	elif 11 in [a,b,c] and sum([a,b,c]) <=31:
		return sum([a,b,c])-10
	else:
		return "BUST"

#return sum of numbers in an array, except ignore sections of numbers starting with 6
#and extending to the next 9. Return 0 for no numbers
def summer_69(arr):
	total = 0
	add = True

	for num in arr:
		while add:
			if num!=6:
				total += num
				break
			else:
				add = False
		while add != True:  # or while not add
			if num != 9:
				break
			else:
				add = True
				break
	return total

#Challenging problems --------------------------

#Spy Game: Write a function that takes in a list of integers 
#and returns True if it contains 007 in order. Does not mean consecutive order

def spy_game(nums):

	code = [0,0,7,'x']
	#[0,7,'x']
	#[7,'x']
	#['x'] Length=1
	for num in nums:
		if num  == code[0]:
			code.pop(0)

	return len(code) == 1

#Count Primes: Write a function that returns the number of prime numbers 
#that exist up to and including a given number

def countPrimes(num):
	#check for 0 and 1 input
	if num < 2:
		return 0

	#2 or greater

	#store out prime numbers
	primes = [2]
	#Counter going up to the input num
	x = 3

	#x is going through every number up to input num
	while x <= num:
		#check if x is prime
		for y in primes: # can use in range(3,x,2)
			if x%y == 0:
				x+=2
				break
		else:
			primes.append(x)
			x += 2
	print(primes)
	return len(primes)










