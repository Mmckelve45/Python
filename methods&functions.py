mylist = [1,2,3]
mylist.append(4)
mylist.pop()

#check the python documentation
help(mylist.append())

#functions
def name_of_function():
	'''
	docstring explains functions
	'''
	print("Hello "+name)
name_of_function("Jose")

def add_function(num1,num2):
	return num1+num2
result = add_function(1,2)


def name_function():
	'''
	DOCSTRING:Information about the function
	INPUT: no input...
	OUTPUT: Hello
	'''
	print("Hello")

name_function()
#prints out Hello
#you can call help on this function

def say_hello(name='NAME'):
	return "Hello "+name
say_hello("Matt") #you get error if you do not pass in paremeter
#if you want you can pass in default name in case not provided

result = say_hello("Zach")

def add(n1,n2):
	return n1+n2
result = add(20,30)


#find out if the word "dog" is in a string
def dog_check(mystring):
	if("dog" in mystring.lower()):
		return True
	else:
		return False
dog_check("my dog ran away")

#this does the same thing
def dog_check(mystring):
	return 'dog' in mystring.lower()

def pig_latin(word):
	first_letter = word[0]
	#check if vowel
	if first_letter in 'aeiou':
		pig_word = word + 'ay'
	else:
		pig_word = word[1:] +first_letter +'ay'
	return pig_word
pig_latin('word')
pig_latin("apple")


#prints out every other letter of the string as uppercase/lowercase
def myfunc(string):
    x=0
    for letter in string:
        if x % 2 == 0:
            print(letter.upper())
        else:
            print(letter.lower())
        x+=1