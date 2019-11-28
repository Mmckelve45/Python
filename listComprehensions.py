mystring = "hello"
mylist = []

for letter in mystring:
	mylist.append(letter)

mylist

#flatten out the forloop
mylist = [letter for letter in mystring]

#spits out ['w','o','r','d']
mylist = [x for x in "word"]

mylist = [num**2 for num in range(0,11)]

mylist = [x**2 for x in range(0,11) if x%2==0]

celcius = [0,10,20,34.5]
farenheit = [( (9/5) * temp + 32) for temp in celcius]

fahrenheit = []
for temp in celcius:
	fahrenheit.append(( (9/5)*temp+32))

#if else in list comprehension
#want to be able to read this shit
results = [x if x%2==0 else 'Odd' for x in range(0,11)]

mylist = []
for x in [2,4,6]:
	for y in [1,10,1000]:
		mylist.append(x*y)

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]

