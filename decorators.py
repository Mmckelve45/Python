#on off switch for certain functionality in functions
#decorators @some_decorator above function

def func():
	return 1

func() 

def hello():
	return "Hello!"
greet = hello
greet()
del hello 

greet() # This still works as it created a copy of the hello function




#the scope of greet and welcome are only inside of the hello function
def hello(name="Matt"):
	print("The hello() Function has been executed!")

	def greet():
		return "\t This is the greet function inside hello!"
	def welcome():
		return "\t This is welcome() inside hello"

	print("I am going to return a function")
	if name == "Matt":
		return greet
	else:
		return welcome

my_new_func = hello("Matt")

#returning a function
def cool():

	def super_cool():
		return "I am very cool!"

	return super_cool
#assigning a function as a variable
some_func = cool()
some_func()



def hello():
	return "Hi Matt"
#passing in a function as an argument
def other(some_def_func):
	print("Other code runs here!")
	print(some_def_func())

other(hello)




#Creating a new decorator
def new_decorator(original_function):

	def wrap_func():

		print("Some Extra code, before the original function")
		original_function()
		print("Some extra code, after the original function!")
	return wrap_func


def func_needs_decorator():
	print("I want to be decorated!!")

func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)

decorated_func()



#same thing as above
@new_decorator
def func_needs_decorator():
	print("I want to be decorated!!")

func_needs_decorator()



