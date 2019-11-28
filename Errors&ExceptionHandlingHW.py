try:
	for i in ['a','b','c']:
		print(i**2)
except TypeError:
	print("This is a Type Error.  Watch out!")
finally:
	print('end')



try:
	x = 5
	y = 0
	z = x/y
except ZeroDivisionError:
	print("cannot divide by 0")
finally:
	print("All done")



def ask():
	while True:
		try:
			num = int(input("Please provide an integer: "))
			newnum = num ** 2
		except:
			print("An error occured! Please try again! \n")
			continue
		else:
			print(f"Thank you for providing an integer. Your number squared is: {newnum}")
			break
		finally:
			print("Done")