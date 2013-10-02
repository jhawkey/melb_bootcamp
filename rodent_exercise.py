from rodents import Rodent

rodents = {}

#Here is the finished solution...

for line in open("rodents.csv"):

	line = line.rstrip()
	tag_id, weight = line.split(',')

	if tag_id not in rodents:
		my_rodent = Rodent(tag_id)
		my_rodent.add_weight(weight)
		rodents[tag_id] = my_rodent

	else:
		rodents[tag_id].add_weight(weight)

print rodents
for key in rodents:
	print rodents[key].tag_id, rodents[key].weights

'''Incorrect first solution I wrote

f = open("rodents.csv", "r")

f_lines = f.readlines()

f.close()

for line in f_lines:

not getting correct output, some weights going in
as a list (correct) but some going in as just values (and aren't correct)

#check to see whether tag_id is in dict
	#if it is,
	if line.split(',')[0] in rodents:
		#add the new weight
		weight = float(line.split(',')[1].rstrip())
		rodents[line.split(',')[0]] = weight
	#if not
	if line.split(',')[0] not in rodents:
		#create a new rodent object
		new_rodent = Rodent(line.split(',')[0])
		weight = float(line.split(',')[1].rstrip())
		new_rodent.add_weight(weight)
		#add the new weight
		rodents[new_rodent.tag_id] = new_rodent.weights

print rodents'''
