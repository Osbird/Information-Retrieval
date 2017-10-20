import random; random.seed(123)
import codecs
import string
import nltk
from nltk.stem.porter import PorterStemmer
import gensim



#Loading file and partitioneing in an array of paragraphs







def file_to_paragraphs(file):
    try:
        f = codecs.open(file, "r", "utf-8");
    except FileNotFoundError:
        print("whoops, that file does not seem to exist")

    paragraph_list = []
    
    paragraph = ""
    for line in f.readlines():
        if "" != line.strip():
            paragraph += line
        else:
            if paragraph!="":
                paragraph_list.append(paragraph)
                paragraph=""

    paragraph_list = [element for element in paragraph_list if "Gutenberg" not in element]

    stemmer = PorterStemmer()

    paragraph_list = [stemmer.stem(paragraph.translate(string.punctuation).lower()) for paragraph in paragraph_list]

    paragraph_tuple = [paragraph.split() for paragraph in paragraph_list]

    return paragraph_tuple

def stemming_and_tupling(String):
    stemmer = PorterStemmer()
    stemmedString = stemmer.stem(String.translate(string.punctuation).lower())
    return stemmedString.split()


def build_dictionary(list_of_paragraphs):
    # returns list of paragraphs as dictionary after removing stemmed stop words
    dictionary = gensim.corpora.Dictionary(list_of_paragraphs)
    return dictionary

def build_and_filter_dict(list_of_paragraphs):
    # Returns a corpus object where each paragraph is a bag of words
    dictionary = build_dictionary(list_of_paragraphs)
    remove_stop_words(dictionary)
    return dictionary

def make_bow(list_of_words):
    dictionary = build_and_filter_dict(list_of_words)
    return dictionary.doc2bow(p) 

def make_bows(list_of_paragraphs):
    dictionary = build_and_filter_dict(list_of_paragraphs)
    return [dictionary.doc2bow(p) for p in list_of_paragraphs]

#Tokenize the paragraphs. We now have a list of paragraphs, where the paragraphs are lists of words

def remove_stop_words(dictionary):
    stopwordsfile = open("common-english-words.txt")
    stopwords = []

    for line in stopwordsfile:
        stopwords.extend(line.split(","))
    
    stop_ids = []
    for word in stopwords:
        if word in dictionary.token2id:
            stop_id = dictionary.token2id[word]
            stop_ids.append(stop_id)

    dictionary.filter_tokens(stop_ids)

def buildTF_IDF(corpus):
    # Return TF-IDF document based on corpus(each paragraph is a bag of words)
    return gensim.models.TfidfModel(corpus)

def bow2TF_IDF(corpus):
    # Maps bags of words into tfidf-weights
    tfidf_corpus = []
    tfidf_model = buildTF_IDF(corpus)
    for bow in corpus:
        tfidf_corpus.append(tfidf_model[bow])
    return tfidf_corpus


def buildLsi(tfidf_corpus, paragraph_tuple):
    return gensim.models.LsiModel(tfidf_corpus, id2word=build_and_filter_dict(paragraph_tuple), num_topics=100)


def bow2Lsi(tfidf_corpus, paragraph_tuple):
    LSI_corpus = []
    LSI_model = buildLsi(tfidf_corpus, paragraph_tuple)
    print (LSI_model.show_topics(3))
    for bow in tfidf_corpus:
        LSI_corpus.append(LSI_model[bow])
    return LSI_corpus

def preproccesing(String):
    dictionary = build_dictionary([String.split()])
    remove_stop_words(dictionary)
    return dictionary.doc2bow(stemming_and_tupling(String))


query = preproccesing("What is the function of money?")

query2 = preproccesing("How taxes influence economics?")

querytf_idf = bow2TF_IDF([query2])

print(querytf_idf)

paragraph_tuple = file_to_paragraphs("theBook_Oving3.txt")


bags_of_words = make_bows(paragraph_tuple)

tfidf_corpus = bow2TF_IDF(bags_of_words)

tfidf_matrixSimilObject = gensim.similarities.MatrixSimilarity(tfidf_corpus)

Lsi_corpus = bow2Lsi(tfidf_corpus, paragraph_tuple)

Lsi_matrixSimilObject = gensim.similarities.MatrixSimilarity(Lsi_corpus)




"""

for i in range(len(filteredList)):
    filteredList[i] = nltk.word_tokenize(filteredList[i])



dictionary = gensim.corpora.Dictionary(filteredList)






paragrapghBows = get_bow(filteredList)


print (paragrapghBows)

tfidf_models = []


#for corpus in paragrapghBows:
#    tfidf_models.append(gensim.models.TfidfModel(corpus))
tfidf = gensim.models.TfidfModel(paragrapghBows[0])

tfidf_corpuses = []

i = 0

for model in tfidf_models:
    tfidf_corpuses.append(tfidf_models[i])
    i+=1


matrixSimililarty = gensim.similarities.MatrixSimilarity(paragrapghBows)

print (matrixSimililarty)
"""