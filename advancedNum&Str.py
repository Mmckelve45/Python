#Hexadecimal
hex(12)
hex(512)


#binary representation
bin(128)
bin(512)


# X^y % z  2^4%3
pow(2,4,3)

abs(-3)
abs(2)

round(3.1)
round(3)
#both of there are 3.0


#rounds to 4
round(3.9)

round(3.141592,2)
#returns 3.14



#----------------------Advance strings

s = "Hello World"
s.capitalize()

s.upper()
s.lower()
s.count("o")

#Finds the first occurence of an o
s.find("o")


#center hello world between z's and 20 total characters
s.center(20,"z")

print("hello\thi").expandtabs()

s = "hello"
s.isalnum() #checks if all the acharacters are alphanumeric (True)

s.isalpha() #is alphabetic?

s.islower()

s.isspace() #all characters are white space

s.istitle() 

s.isupper() #True if all characters are uppercase

s.endswith("o") # s[-1] == 'o'

s.split("e")

#gives first part, seperator, and tail end
s.partition("l")