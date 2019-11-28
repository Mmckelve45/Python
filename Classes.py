class Line:

	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		x1,y1 = self.coor1
		x2,y2 = self.coor2
		return((x2-x1)**2 + (y2-y1)**2)**0.5
	def slope(self):
		x1,y1 = self.coor1
		x2,y2 = self.coor2

		return (y2-y1) / (x2-x1)

myline = Line((3,2),(8,10))
myline.distance()
myline.slope()


class Cylinder:

	def __init__(self,height=1,radius=1):
		self.height = height
		self.radius = radius

	def volume(self):
		return self.height * 3.14 * (self.radius)**2

	def surface_area(self):
		top = 3.14 * (self.radius**2)
		return (2*top) + (2*3.14*self.radius*self.height)



class Simple():

	def __init__(self,value):

		self.value = value

	def add_to_value(self,amount):
		self.value = self.value + amount
		print("We just added {} to your value".format(amount))

myobj = Simple(300)
myobj.value
myobj.add_to_value(500)

myobj.value