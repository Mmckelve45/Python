st = "print only the words that start with s in this sentence"
stSplit = st.split()
for word in stSplit:
	if word[0] == 's':
		print(word)

for num in range (0,11):
	if num % 2 == 0:
		print(num)

myList = [x for x in range(1,50) if x%3 == 0]

sent = "Print every word in this sentence that has an even number of letters"
sentSplit = sent.split()
for word in sentSplit:
	if len(word) % 2 == 0:
		print(word)

for num in range(1,101):
	if num % 3 == 0 and num % 5 == 0:
		print("FizzBuzz")
		continue
	elif num % 5 == 0:
		print("Buzz")
		continue
	elif num % 3 == 0:
		print("Fizz")
		continue
	else:
		print(num)

st2 = "create a list of the first letter of every word in this string"
listSplit = [x[0] for x in st2.split()]
