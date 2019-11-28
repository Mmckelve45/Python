from collections import defaultdict
d = {'k1':1}
d["k1"] # returns 1

d["k2"] # gives a KeyError

d = defaultdict(object)
d["one"]

for item in d:
	print item

d = defaultdict(lambda: 0)
d["one"] #returns 0
d["two"] = 2





#----------------------Ordered Dictionaries------------------
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k,v in d.items():
	print k,v

#The normal dictionary is just a mapping so there is no particular order but you can import an ordered dictionary
from collections import OrderedDict

d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k,v in d.items():
	print k,v


d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d1['a'] = 1
print d1 = d2 #Returns True





d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d1['a'] = 1
print d1 = d2 #Returns False