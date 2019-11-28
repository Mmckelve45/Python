t = (1,2,3)
t[0]

from collections import namedtuple

Dog = namedtuple('Dog','age breed name')

sam = Dog(age=2,breed="lab",name="Sammy")
sam.age

Cat = namedtuple("Cat", 'fut claws name')

c = Cat(fur = "fuzzy", claws = False, name = "Kitty")
c[1]
c[2]