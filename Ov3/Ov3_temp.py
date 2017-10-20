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