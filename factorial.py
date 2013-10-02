def factorial(n):

#add 1 to n value so range function has proper end value
	newn = n+1
	
	#list of values which are going to be multiplied
	range_n = range(1, newn)
	
	#first number to be multiplied (so not 0)
	result = range_n[0]
	
	#multiply the rest of the values to the first
	for i in range_n[1:]:
		result *= i
	
	return result

#print factorial(0)
#print factorial(1)
print factorial(3)
print factorial(5)

#better way, because above can't deal with the factorial of 0 or 1
# def factorial(n):
	#if n <= 1:
		#return 1
	#else:
		#return n * factorial(n-1)
