
#requirements nltk
#code in python 3.6



from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string


def names(text):
    twords = word_tokenize(text)
    stop_words = stopwords.words('english') +  list(string.punctuation)
    names = []
    for n,word in enumerate(twords):
        if word not in stop_words:
            if len(wn.synsets(word)) == 0 : #or check if name in common list of words
                if len(names)==0: 
                    names.append([n,word])
                elif names[-1][0] == (n - 1) :
                    names[-1][1] = str(names[-1][1]) + " " + str(word)
                else :
                    names.append([n,word])
    return names
    
    
#example    
#text = "hi umasai,mohit, eric,himanshu kumar and vaibav are doing some work . please #get back to divya"    
#print(names(text))
#
#
#
#result - [[1, 'umasai'],
# [3, 'mohit'],
# [5, 'eric'],
# [7, 'himanshu kumar'],
# [10, 'vaibav'],
# [20, 'divya']]