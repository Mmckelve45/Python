def myfunc(a,b):
	#Returns 5 % of the sum of a and b
	return sum((a,b))*0.05
myfunc(40,60)

def myfunc(a,b,c=0,d=0,e=0): # default is 0
	return sum((a,b,c,d,e)) * 0.05

def myfunc(*args): #treats this as a tuple of parameters coming in
	print(args)
myfunc(40,60,100,1,34)

#build a dictionary of key arguments
def newfunc(**kwargs):
	if "fruit" in kwargs:
		print("My fruit of choise is {}".format(kwargs['fruit']))
	else:
		print("I did not find any fruit here")

newfunc(fruit = "apple", veggie = "lettuce")

#using both at the same time
#allows you to take in an arbitraryu number of arguments
#powerful when you are using multiple libraries
def bothfunction(*args, **kwargs):
	print("I would like {} {}".format(args[0],kwargs["food"]))

bothfunction(10,20,30, fruit="orange", food="eggs",animal="dog")

def myfunc(*args):
    return sum(args)