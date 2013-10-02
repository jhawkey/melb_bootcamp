import string

class InvalidBaseException(Exception):
	pass

class ZeroLengthSequenceException(Exception):
	pass

try:
	#do something
	pass
except InvalidBaseException:
	pass
except ZeroLengthSequenceException:
	pass

class NucleotideSequence:
	'''An abstract class which is inherited by DNASequence or
	RNASequence. Not for general use. Use DNASequence and RNASequence
	instead.'''

	complements = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}
	valid = set(complements)

	def __init__(self, sequence):
		'''Input sequence should be a string in all
		uppercase.'''
		#check sequence is string
		#assert isinstance(sequence, str)
		if not type(sequence) == str:
			raise Exception('Input must be a string')
		
		#check it's uppercase and, can also make uppercase
		#assert sequence.isupper()
		sequence = sequence.upper()
		
		#check sequence length isn't 0
		if len(sequence) <= 0:
			raise Exception('Input must be a string with 1 or more characters')
		#assert len(sequence) > 0
		
		#check all bases in sequence are valid
		#assert set(sequence).difference(self.valid) == set()
		if set(sequence).difference(self.valid) != set():
			raise InvalidBaseException("Invalid base, base: " +  ''.join(set(sequence).difference(self.valid)))
		
		self.sequence = sequence
		
		#can create a base_counts dict to save recomputing bases for 
		#a sequence if it's been done already -- reduces runtime
		#this is an OBJECT
		self.base_counts = {}

	def base_count(self, base):
		'''Given a base, return the number of times
		the base occurs in this sequence. Returns an integer.'''
		
		#chek base is string, that it's only 1 base and it's a valid base
		assert isinstance(base, str)
		assert len(base) == 1
		assert base in self.valid
		
		if base in self.base_counts:
			return self.base_counts[base]
		
		else:
			count = self.sequence.count(base)
			self.base_counts[base] = count
			
			return count

	def gc_content(self):
		'''Calculates the GC content of a sequence. Returns a percentage.'''
		
		#return (base_count(self, 'G') + base_count(self, 'C')) / float(len(self))
		g=self.base_count('G')
		c=self.base_count('C')
		
		return (float(g+c) / len(self.sequence)) * 100

	def reverse_complement(self):
		'''Reverses sequence and then complemenents it 
		(G's become C's, A's become T's, etc), then returns
		the new sequence.'''
		
		#can do with a dictionary which has been set above (complements)
		rev_c = ""
		
		for base in self.sequence:
			rev_c = self.complements[base] + rev_c
		
		return rev_c

		'''#reverse sequence
		rev = self.sequence[::-1]
		#turn G's to C's and A's to T's
		trans_tab = string.maketrans('ATCG', 'TAGC')
		return rev.translate(trans_tab)'''

class DNASequence(NucleotideSequence):
	'''Uses the bases GTAC.'''

	def __init__(self, sequence):
		NucleotideSequence.__init__(self, sequence)
		if 'U' in sequence:
			raise Exception("DNA sequence must contain T's instead of U's")

class RNASequence(NucleotideSequence):
	'''Uses the bases GUAC.'''
	
	complements = {'G': 'C', 'C': 'G', 'U': 'A', 'A': 'U'}
	valid = set(complements)
	
	def __init__(self, sequence):
		NucleotideSequence.__init__(self, sequence)
		if 'T' in sequence:
			raise Exception("RNA sequence must contain U's instead of T's")

