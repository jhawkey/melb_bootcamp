import sys
import string

#get sentence
sentence = sys.argv[1]

#turn to lowercase, remove final punctuation
lowercase = sentence.lower()

#make set
letter_set = set(lowercase)

#create set of punctuation characters that are unwanted
#punctuation_list = [',', '!', '?', "'", '"', '.', ' ']
#punctuation_set = set(punctuation_list)

punctuation_set = set(" .,!?'")

#better way to get all letter characters rather than definining unwanted
#characters explicitly
alphabet = string.lowercase

#remove space characters and punctuation
no_punctuation = letter_set.difference(punctuation_set)

#find the intersection of the letter set with allowed characters
letters = letter_set.intersection(alphabet)

#print output
print len(no_punctuation)
print len(letters)
