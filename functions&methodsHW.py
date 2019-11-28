#Write a function that computers the voume of a sphere given its radius
def volume(rad):
	return (4/3)*3.14*(rad**3)

#write a function that checks whether a number is in a given range(inclusive of high and low)
#One for Boolean and on printing it out

def ran_check(num,low,high):
	#could also say if num in range(low,high):
	if low <= num <= high:
		print(f"{num} is in the range between {low} and {high}")
	else:
		print("Number does not fall within the range given")

def bool_check(num,low,high):
	#return num in range(low,high)
	return low <= num <= high

#write a function that accepts a string and calculates the number of upper case letters and lower case letters
def stringcalc(text):
	countLower = 0
	countUpper = 0
	for i in range(0,len(text)):
		if text[i] == text[i].lower():
			countLower += 1
		else:
			countUpper += 1
	print(f"{countLower} lowercase letters and {countUpper} upper case letters")
	return countLower
	return countUpper

def up_low(s):
	d={"upper":0, "lower":0}
	for c in s:
		if c.isupper():
			d["upper"]+=1
		elif c.islower():
			d["lower"]+=1
		else:
			pass
		print "Original String: ", s
		print "No. of Upper case characters : ",d["upper"]
		print "No. of Lower case characters : ",d["lower"]


#write a function that takes a list and returns a new list with unique elements of the first list
def setlist(nums):
	uniqueList = set(nums)
	return list(uniqueList)

def unique_list(1):
	x = []
	for a in 1:
		if a not in x:
			x.append(a)
	return x


#function to multiply all the numbers in a list
def multlist(nums):
	total = 1
	for i in range(-1,len(nums)-1):
		total *= nums[i+1] 
	return total

def multiply(numbers):
	total = numbers[0]
	for x in numbers:
		total *= x
	return total


#write a function to check if a word or a phrase reads the same backwards as forwards (palindrome)
def palindrome(s):
	return s == s[::-1]


#function to check if a string is a pangram or not (contains every letter of the alphabet)
import string
def ispangram(str1, alphabet = string.ascii_lowercase):
	alphaset = set(alphabet)
	return alphaset <= set(str1.lower())
