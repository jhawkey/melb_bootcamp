f = open("uniprot_sprot.fasta", "r")

#set variable to count no of human proteins
count = 0

#go through each line of the file
while True:
	line = f.readline()

#if you get to the end of the file then break the loop
	if not line:
		break
#look for header of fasta and also look to see if protein is human
#if it is then add one to count variable
	if line[0] == '>' and "OS=Homo sapiens" in line:
		count += 1

#close the file
f.close()

#print the result
print "There are " + str(count) + " human proteins in Swiss Prot"
