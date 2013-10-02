file_name = "test.csv"
default_file = "rodents.csv"

try:
	file = open(file_name)

#adding the IOError means that this block will only be executed
#in case of IOError, not another type of error
#e is the name of the error which will be printed using the print statement 
#on line 12
except IOError as e:
	print e
	file = open(default_file)

#execute this block if there is another error that isn't IOError
except:
	print 'There was some other problem'
	raise

print file.readline()
