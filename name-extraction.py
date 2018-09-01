
#requirements nltk
#code in python 3.6



from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re
replacingwords = ['.', '-']
Punclist = ['’','“','”','would','could','since']

#this fuction finds all probable names(duplicates included) and numbers in a given text and returns
#2 dictionaries names and numbers respectively

def names(text):
    compiles = re.compile('|'.join(map(re.escape, replacingwords)))
    uptex = compiles.sub(" ", text)
    twords = word_tokenize(uptex)
    stop_words = stopwords.words('english') +  list(string.punctuation) + Punclist
    names = {}
    nums = {}
    for n,word in enumerate(twords):
        if word.lower() not in stop_words:
            if word.isnumeric():
                nums[n] = word
            if len(wn.synsets(word)) == 0 and not word.isnumeric(): #or check if name in common list of words
                names[n]=word
    return names,nums


#this fuction takes the names dictionary from names fuction and joins these
#names based on the position of then in text

#this fuction returns a set of all joined names


def fullnames(na):
    lis = list(na.keys())

    fullnames = {}
    for k in lis:
        fullnames[k] = na[k]
        if k+1 in lis:
            fullnames[k] = fullnames[k] + " " + na[k+1]
            lis.remove(k+1)
        if k+2 in lis:
            fullnames[k] = fullnames[k] + na[k+2]
            lis.remove(k+2)
            
    #uncomment below code if names have more than 3 words
    #     if k+3 in lis:
    #         fullnames[k] = fullnames[k] + na[k+3]
    #         lis.remove(k+3)
    
    return set(fullnames.values())    


    
#example :-    
#text = "hi umasai,mohit, eric,himanshu kumar and vaibav are doing some work . please get back to divya"    
##usage
#namedict,numberdict = names(text) #gives 2 dictionaries with names and numers
#joinednames  = fullnames(namedict)
#print(joinednames)
#
#
#
#result - {'umasai','mohit','eric','himanshu kumar', 'vaibav','divya'}
