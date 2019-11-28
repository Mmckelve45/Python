myList = [1,2,3]

#prints numers starting at 3 up to but not including 10, then step size is third argument
for num in range(3,10,2):
	print(num)

#generates a list and doesn't save this to memory
list(range(0,11,2))

index_count = 0

for letter in 'abcde':
	print('At index {} the letter is {}'.format(index_count,letter))
	index_count += 1

#will output a,b,c,d,e
index_count = 0
word = 'abcde'
for letter in word:
	print(word[index_count])
	index_count += 1

#enumerate funciton (made because it is common)
#returns these as tuples (0,'a') (1,'b') ect
word = 'abcde'
for item in enumerate(word):
	print(item)

#zip function

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
#zips together the list and pairs the items (you can use more than just 2 lists)
for item in zip (mylist1,mylist2):
	print(item)

list(zip(mylist1,mylist2))

#in operator
'x' in [1,2,3]
"x" in ["x","y","z"]
'a' in 'a world'
'mykey' in {'mykey':345} #True
d = {"mykey" :345}
345 in d.values() #True
345 in d.keys() #False

mylist = [10,20,30,40,100]
min(mylist)
max(mylist)

from  random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
mylist 
type(mylist) #returns NoneType

from random import randint
randint(0,100)
mynum = randint(0,10)
mynum

result = input("Enter a number here: ")
result #returns Matt
#This always passes back a string
#you can use int(result) or float(result)

result = int(input("Favorite Number: "))

