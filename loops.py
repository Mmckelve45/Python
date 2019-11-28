
#the naming doesnt matter
myList = [1,2,3,4,5,6,7,8,9,10]
for jelly in myList:
	print("Yo")

tup = (1,2,3)
for item in tup:
	print(item)

myList = [(1,2),(3,4),(5,6),(7,8)]
len(myList) # returns 4 (4 pairs)

#tuple unpacking 
#you actually don't need the parenthesis below
for (a,b) in myList:
	print(a)

d = {'k1':1,'k2':2,'k3':3}

#This only iterates through the keys
for item in d:
	print(item)
#same tuple unpacking stuff
for key,value in d.items():
	print(value)

#------------While Loops--------------#
x = 0

while x < 5:
	print(f'Teh current value of x is {x}')
	x+=1 #same as x = x+1
else:
	print("X is not less than 5")

#break, continue, and pass
#break: breaks out of the current enclosing loop
#continue: goes to the top of closest enclosing loop
#pass: Does nothing at all.

x = [1,2,3]
for item in x:
	pass #means do nothing at all (placeholder)

print("end of my script")

mystring = "Matt"
for letter in mystring:
	if letter == 'a':
		continue #if the letter is a then go back to looping through		
	print(letter)

mystring = "Matt"
for letter in mystring:
	if letter == 'a':
		break #Stops the loop when letter 'a' gets hit
	print(letter)

x = 0
while x < 5:
	if x == 2:
		break
	print(x)
	x+=1

