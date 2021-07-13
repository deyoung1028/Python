value1 = int(input('Enter a number'))
value2 = int(input('Enter a number'))
operation = input("Operation [+], [-],[*],[/]:")

def addition(value1,Value2):
    print("%d + %d" % (value1, value2))
    sum = value1 + Value2
    return sum

def subtraction(value1, value2):
	print("%d - %d" % (value1, value2))
	difference = value1 - value2
	return difference

def multiplcation(value1, value2):
	print("%d * %d" % (value1,value2))
	product = value1 * value2
	return product

def division(value1, value2):
	print("%d / %d" % (value1, value2))
	remainder = value1 / value2
	return remainder

def calculate():
	if (operation == "+"):
		total = addition(value1, value2)
	elif (operation == "-"):
		total = subtraction(value1, value2)
	elif (operation == "*"):
		total = multiplcation(value1, value2)
	elif (operation == "/"):
		total = division(value1, value2)
	print(total)

calculate()
	




