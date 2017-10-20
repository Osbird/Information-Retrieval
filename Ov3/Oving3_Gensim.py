import random; random.seed(123)
import codecs


partitionedFile = []
linenum = int
try:
    f = codecs.open("theBook_Oving3.txt", "r", "utf-8");
    entirefile = f.read()
    partitionedFile = entirefile.split('\n')
except FileNotFoundError:
    print("whoops, that file does not seem to exist")
print(partitionedFile)
print(len(partitionedFile))