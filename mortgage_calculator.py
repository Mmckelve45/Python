#Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
#Also figure out how long it will take the user to pay back the loan. 
#For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
#monthly_pmt = int(input("What is your monthly Payment? "))


#Don't need this function but can use it inside of the mortgage calc instead of using parameters or use for reference instead.
def questions():
	borrowed = int(input("How much money did you borrow? "))
	int_rate = int(input("What is the annual interest rate? "))
	total_months = int(input("How many months will you be repaying this mortgage? "))
	return borrowed, int_rate, total_months





def mortgage_calc(borrowed, int_rate, total_months):

	months_remaining = total_months
	interest = int_rate/12

	total_remaining = borrowed 

	monthly_principal_pmt = borrowed / total_months
	monthly_interest_pmt = interest * total_remaining
	total_monthly_pmt = monthly_principal_pmt + monthly_interest_pmt
	
	for i in range(1,total_months+1):
		print(f"{i}. Your total monthly principal payment is ${round(monthly_principal_pmt,2)}") 
		print(f"{i}. Your total monthly interest payment is ${round(monthly_interest_pmt,2)}")
		print(f"{i}. Your total payment for the month is ${round(total_monthly_pmt,2)}")

		total_remaining -= monthly_principal_pmt
		monthly_interest_pmt = interest * total_remaining
		total_monthly_pmt = monthly_principal_pmt + monthly_interest_pmt
		print(f"{i}. ${round(total_remaining,2)} remaining principal to pay off!")
		print("\n \n")


