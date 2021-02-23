# Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. 
# However, your function cannot use the multiplication, modulo, or division operators.

def is_even(k):
	if (k & 1 == 0):
		return True
	else:
		return False

try:
	a = int(input("Enter a number: "))
	if is_even(a) is True:
		print ("Number is Even")
	elif is_even(a) is False:
		print ("Number is Odd")
except ValueError as err:
	print (err)
