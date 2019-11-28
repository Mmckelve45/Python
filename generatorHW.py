def gensquares(n):
	for x in range(n):
		yield x ** 2

for x in gensquares(10):
	print(x)




import random
def ran_num(n, low, high):
	for x in range(n):
		yield random.randint(low,high)

for num in rand_num(12,1,10):
	print(num)



s = "Hello"
s_iter = iter(s)
print(next(s))
