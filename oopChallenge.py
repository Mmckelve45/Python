class Simple():

	def __init__(self,value):

		self.value = value

	def add_to_value(self,amount):
		self.value = self.value + amount

myobj = Simple(300)
myobj.value
myobj.add_to_value(500)

myobj.value


class Account():

	def __init__(self,owner,balance=0):
		self.owner = owner
		self.balance = balance

	def deposit(self, depositamount):
		self.depositamount = depositamount
		print(f"added {self.depositamount} to the balance")
		self.balance += self.depositamount
		print("Deposit Accepted")
		return self.balance


	def withdrawal(self, takeamount):
		self.takeamount = takeamount

		if (self.balance-self.takeamount) >= 0:
			print("Withdrawal Accepted")
			self.balance -= self.takeamount
		else:
			print(f"Insufficient Funds. {self.owner} only has ${self.balance} available for use. ")
		return self.balance

	def __str__(self):
		return f"Owner: {self.owner} \nBalance: {self.balance}"



