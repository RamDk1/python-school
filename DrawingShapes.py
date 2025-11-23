# Python code​​​​​​‌‌‌​‌​‌​​‌‌​‌​​‌‌‌‌‌‌‌​‌​ below
class Shape:
	width = 5
	height = 5
	printChar = '#'

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
	def printRow(self,i):
		print(self.printChar * (i + 1))
	pass

s=Square()
s.print()
t=Triangle()
t.print()