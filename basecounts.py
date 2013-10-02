import sys

sequence = sys.argv[1]

sequence = sequence.upper()

base_counts = {}

base_counts['G'] = sequence.count('G')
base_counts['A'] = sequence.count('A')
base_counts['T'] = sequence.count('T')
base_counts['C'] = sequence.count('C')
base_counts['U'] = sequence.count('U')

GC_content = float((base_counts['G'] + base_counts['C'])) / float((base_counts['A'] + base_counts['G'] + base_counts['T'] + base_counts['C'] + base_counts['U'])) * 100

print base_counts
print GC_content

#better method: g = sequence.count('G') etc, then total_length = g+t+a+c,
#so gc_content = (g+c)/float(total_length)*100 and
#base_counts = {'G': g, 'A': a. 'T': t, 'C': c}
