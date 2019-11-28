

def create_cubes(n):
	result = []
	for x in range(n):
		result.append(x**3)
	return result

create_cubes(10)



#here we only needed one value at a time.  Does not need to create a giant list of memory
for x in create_cubes(10):
	print(x)



#create_cubes is way more memory efficient this way
def create_cubes(n):
	for x in range(n):
		yield x**3

for x in create_cubes(10):
	print(x)



#yielding it is much more memory efficient
list(create_cubes(10))




#you can hold things in memory (store in list) or yield it for later use
def gen_fibon(n):

	a = 1
	b = 1
	#output = []
	for i in range(n):
		yield a
		#output.append(a)
		a,b = b,a+b
	#return output

for number in gen_fibon(10):
	print(number)




def simple_gen():
	for x in range(3):
		yield x

for num in simple_gen():
	print(number)

g = simple_gen()
print(next(g))
#remembers the previous number
print(next(g))
#remembers the previous number
print(next(g))

# automatically iterate through object
s = "Hello"
for letter in s:
	print(letter)
next(s) #error.  The string object needs to be converted into an iterable object
s_iter = iter(s)
next(s_iter)