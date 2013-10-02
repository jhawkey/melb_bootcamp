def base_count(sequence, base):
	
	return sequence.count(base)


def gc_content(sequence):

	return (base_count(sequence, 'G') + base_count(sequence, 'C')) / float(len(sequence))


