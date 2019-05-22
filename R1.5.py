# Write a short Python function that takes a positive integer n
# and returns the sum of the squares of all the positive integers smaller than n
# relying on Python's comprehension syntax and the built-in sum function.

n = int(input("Enter the number..."))
total = sum((k*k) for k in range (1, n+1))
print (total)
