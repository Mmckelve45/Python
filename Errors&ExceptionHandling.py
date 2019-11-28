def add(n1,n2):
	print(n1+n2)

number1 = 10
number2 = input("Please provide a number: ")
add(number1,number2) #produces an error becase the input return is a string
print("Something happened!") #This will not run because there was an error before it




try:
	# WANT TO ATTEMPT THIS CODE
	#MAY HAVE AN ERROR
	result = 10 + '10'
except:
	#what happens if there is an error
	print("Hey it looks like you aren't adding correctly!")
else: #if there is no error
	print("Add went well!")
	print(result)



try:
	f = open("testfile","r")
	f.write("Write a test line")
except TypeError: #except for a specific type error
	print("There was a type error")
except OSError:
	print("Hey you have an OS Error")
except: #grabs all other errors
	print("All other exceptions")
finally: #executes no matter what
	print("I always run")



def ask_for_int():
	try:
		result = int(input("Please provide a number: "))
	except:
		print("Whoops! That is not a number")
	finally:
		print("End of try/except/finally")

ask_for_int()


#with a while loop
def ask_for_int():
	while True:
		try: #try this code
			result = int(input("Please provide a number: "))
		except: #if error, say whoops
			print("Whoops! That is not a number")
			continue
		else: #if run correctly
			print("Yes thank you")
			break
		finally:
			print("End of try/except/finally")
			print("I will always run at the end")
			print("I am going to ask you again")
ask_for_int()

