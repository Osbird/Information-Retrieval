import random; random.seed(123)
import codecs
<<<<<<< HEAD
import string

print (string.punctuation+"\n\r\t")
=======
import nltk
>>>>>>> d722d2c94695a85f9b2398e94152ea5ebc0ca3ab


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

partitionedFile = [paragraph.translate(string.punctuation).lower() for paragraph in partitionedFile]






print (partitionedFile[-5:])

#Tokenize the paragraphs. We now have a list of paragrahs, where the paragraphs are lists of words
#Tokenize the paragraphs. We now have a list of paragraphs, where the paragraphs are lists of words
for i in range(len(filteredList)):
    filteredList[i] = nltk.word_tokenize(filteredList[i])
