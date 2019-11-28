x = 25
def printer():
	x = 50
	return x
print(x) #returns 25

print(printer())
#this is because of scope.

#LEGB Rule

#L:Local - Names assigned any way within a function (def or Lambda), and not declared gloabal in that function
#E:Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda, from inner to outer)
#G:Global(module) - names assigned at the top-level of a module file, or declared global in a def within a file
#B:Build-in(python) - names preassigned in the built-in names module:open,range,Syntaxerror

#Local - num is local to the lambda expression
lambda num:num**2 

#Enclosing - Looks locally and then globally

name = "This is a global String" #Global
def greet():

	#Enclosing
	name = "Sammy"
	def hello():
		#Local
		name = "I am a local"
		print("Hello " +name)
	hello()

greet()


x = 50
def func(x):
	print(f'X is {x}')
func(x) # X is 50

def func(x):
	print(f'X is {x}')
	x = 200
	print(f'I just locally changed x to {x}')
func(x) # X is 50 #I just locally changed x to 200
print(x) # x is still 50



#If you acually want your x to be reassigned globally while still in the function
x = 50
def func(x):
	global x 
	print(f'X is {x}')

	#local reassignment ON A GLOBAL VARIABLE
	x = 'New Value'
	print(f'I just locally changed x to {x}')

print(x) # x is still 50
func(x) # X is 50 # I just locally changed x to New Value

x = func(x) #avoid using this global keyword and use this as a reassignment
#just have the function return something
