# Write a short Python function that takes a positive integer n
# and returns the sum of the squares of all the positive integers smaller than n.

n = int(input("Enter the number..."))
sum=0
for i in range (1,n+1):
    sum = sum + i*i

print (sum)
