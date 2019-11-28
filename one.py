#One.py
#to call at command line python pythonfile.py
#anything at indentation level 0 gets run
#there is no main function that calls everything else. Everything at indentation 0 gets called
#python has a built in variable called __name__
#if __name__ == "__main__": #python does this in the background


def func():
	print("Func() in one.py")

def function():
	pass
def function2():
	pass

if __name__ == "__main__":
	#Run the script
	function()
	function2()