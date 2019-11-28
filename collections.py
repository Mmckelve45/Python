#Counter - Dictionary subclass
from collections import Counter

l - [1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5]

Counter(l)

s = "asdasdasdasdasdfg"
Counter(s)

s = "How many times does each word show up in this sentence word word show up up show"
words = s.split()

Counter(words)

c = Counter(words)
c.most_commmon(2)


sum(c.values()) #total of all counts
c.clear()   #reset all counts
list(c)  # list of unique elements
set(c) # Convert to a set
dict(c) # convert to a regular dictionary
c.items() #convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))  #convert from a list of (elem, cnt) pairs 
c.most_common()[:-n-1:-1] #n least common elements
c += Counter()  #remove zero and negative counts

sum(c.values()) # total words in string
