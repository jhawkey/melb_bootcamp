import doctest

def factorial(n):
	'''Returns the factorial of an integer. 
	Integer must be a non negative number.
	
	F(N) = F(N) * F(N-1) * F(N-2) ....
	F(1) = 1, F(3) = 6
	
	>>> factorial(0)
	1
	>>> factorial(1)
	1
	>>> factorial(3)
	6
	'''
	
	#assertion doesn't tell a lot, just says that it fails
	#might not be obvious what's gone wrong
	#assert n >= 0
	#assert isinstance(n, int)
	
	#cant use if not isinstance(n, int) as booleans are also int
	#this definition is more explicit
	if not type(n) == int:
		raise Exception('Input must be an integer')
	if n < 0:
		raise Exception('Factorial for negative numbers is not defined')
	
	total = 1
	for i in range(1,n+1):
		total *= i
	return total


def fibonacci(n):
#better to do tests in the docstring
	'''Returns the Nth value in the Fibonacci sequence.
	
	F(N) = F(N-1) + F(N-2)
	F(0) = 0, F(1) = 1
	
	>>> fibonacci(0)
	0
	>>> fibonacci(1)
	1
	>>> fibonacci(2)
	1
	>>> fibonacci(5)
	5
	'''
	
	assert n >= 0
	assert isinstance(n, int)
	
	a, b = 0, 1
	while n > 0:
		a, b = b, a+b
		n -= 1
	return a

#an if condition which will only run the tests if the module is being run on
#its own, not if it's being used by something else
if __name__ == "__main__":
	doctest.testmod()

'''take a list of lists called tests, value 1 is input
and value 2 is expected result, then loop through --> not
very efficient.

for input, expected_result in tests:
	assert fibonacci(input) == expected result'''
