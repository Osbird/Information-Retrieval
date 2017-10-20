import random; random.seed(123)
import codecs


partitionedFile = []

#Partitioning the file into paragraphs
try:
    f = codecs.open("theBook_Oving3.txt", "r", "utf-8");
    entireFile = f.read()
    partitionedFile = entireFile.split('\s{4,}',entireFile)
except FileNotFoundError:
    print("whoops, that file does not seem to exist")

#Filter the list, excluding headers and footers
filteredList = [element for element in partitionedFile if "guthenberg" not in element]

print(len(partitionedFile))
print(len(filteredList))


import random; random.seed(123)
import codecs
import nltk


partitionedFile = []
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
print(filteredList[0:20])

#Tokenize the paragraphs. We now have a list of paragraphs, where the paragraphs are lists of words
for i in range(len(filteredList)):
    a=0