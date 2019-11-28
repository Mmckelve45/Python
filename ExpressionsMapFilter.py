#Lambda Expresions (one time use functions)
def square(num):
	return num**2
my_nums = [1,2,3,4,5]

map(square,my_nums)
for item in map(square,my_nums):
	print(item)
list(map(square,my_nums))

def splicer(mystring):
	if len(mystring)%2 == 0:
		return "EVEN"
	else:
		return mystring[0]
names = ['Andy','Eve','Sally']


# you do not add in () because you are passing in the function as an argument
list(map(splicer,names)) 

def check_even(num):
	return num % 2 == 0

mynums = [1,2,3,4,5,6]
filter(check_even,mynums)

list(filter(check_even,mynums))


def square(num):
	result = num**2
	return result
square(3)

#Lambda Expression
def square(num): return num ** 2
lambda num: return num ** 2
square = lambda num: num**2
square(5)

#used in conjunction with map and filter
mynums = [1,2,3,4,5,6]
names = ['Andy','Eve','Sally']
list(map(lambda num:num**2,mynums))
list(filter(lambda num: num%2 ==0,mynums))

list(map(lambda x:x[0],names))
list(map(lambda x:x[::-1],names))
