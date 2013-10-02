from dna_sequence import DNASequence, RNASequence

def enter_seq():
	x = ''
	while x == '':
		try:
			x = DNASequence(raw_input('Enter sequence here: '))
		except:
			pass
	return x

print enter_seq()

'''
try:
	sequence = DNASequence(x)
except:
	x = raw_input('Invalid input, try again: ')
	sequence = DNASequence(x)
'''
