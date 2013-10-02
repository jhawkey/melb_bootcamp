import sys

value = int(sys.argv[1])

if value > 0 and value < 50:
	print 'Minor'
elif value >= 50 and value < 1000:
	print 'Major'
else:
	print 'Severe'
