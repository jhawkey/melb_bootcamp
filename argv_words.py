import sys

#get words
word_list = sys.argv[1:]

#sort alphabetically
word_list.sort()

#join words, seperated by a comma, but only if not the last word
for word in word_list:
	if word != word_list[-1]:
		output = ', '.join(word_list[0:-1])
#last word is added seperately
	else:
		output += ' and '+ word_list[-1] + '.'

print output

