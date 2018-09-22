def minmax(data):
	biggest = data[0]
	smallest = data[0]
	for i in range (0,len(data)):
		if data[i] > biggest:
			biggest = data [i]
		elif data [i] < smallest:
			smallest = data[i]
	return biggest, smallest

data1 = [2,3,6,119,-22,-23]
print (minmax(data1))

data2 = [2,2,2,2]
print (minmax(data2))


data3 = [2]
print (minmax(data3))


data4 = [50,-50, 500, 1000, -222]
print (minmax(data4))