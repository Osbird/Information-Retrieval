import random; random.seed(123)
import codecs
import string
import nltk



#Loading file and partitioneing in an array of paragraphs
try:
    f = codecs.open("theBook_Oving3.txt", "r", "utf-8");
    entirefile = f.read()
    partitionedFile = entirefile.split('\n ')
except FileNotFoundError:
    print("whoops, that file does not seem to exist")
print(len(partitionedFile))


#Filter the array to exclude elements containing the word "Guthenberg"
filteredList = [element for element in partitionedFile if 'Gutenberg' not in element]
print("Filtrert liste")

print(len(filteredList))

filteredList = [paragraph.translate(string.punctuation).lower() for paragraph in filteredList]

print (partitionedFile[-5:])

#Tokenize the paragraphs. We now have a list of paragraphs, where the paragraphs are lists of words
for i in range(len(filteredList)):
    filteredList[i] = nltk.word_tokenize(filteredList[i])


