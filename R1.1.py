def is_multiple(n,m):
	try:
		if (n % m == 0):
			print ('First number is a multiple of Second number.')
		else:
			print ('First number is not a multiple of Second number.')
	except ZeroDivisionError as e:
		print ("Division by zero is not allowed. Error: ", e)



n = int(input('Enter first number: '))
m = int(input('Enter second number: '))

is_multiple (n,m)
