import random; random.seed(123)
import codecs


partitionedFile = []
linenum = int
try:
    f = codecs.open("theBook_Oving3.txt", "r", "utf-8");
    read = f.readline()
    temporaryString = ""
    while read != '':
        if read == "\n":
            print(1)
            partitionedFile.append(temporaryString)
            temporaryString = ""

        else:
            temporaryString = temporaryString + "\n" + read
            #print(temporaryString)

        print(read)
        read=f.readline()

except FileNotFoundError:
    print("whoops, that file does not seem to exist")


print(partitionedFile)


g = codecs.open("theBook_Oving3.txt", "r", "utf-8");
entirefile = g.read()
paragr = entirefile.split('\s{4,}')