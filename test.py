from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re
class namextract:
    def __init__(namelist=[]):
        cnames = namelist
        replacingwords = ['.', '-']
        Punclist = ['’','“','”','would','could','since']
        
    def names(self,text):
        compiles = re.compile('|'.join(map(re.escape, self.replacingwords)))
        uptex = compiles.sub(" ", text)
        twords = word_tokenize(uptex)
        stop_words = stopwords.words('english') +  list(string.punctuation) + self.Punclist
        names = {}
        nums = {}
        for n,word in enumerate(twords):
            if word.lower() not in stop_words:
                if word.isnumeric():
                    nums[n] = word
                if (len(wn.synsets(word)) == 0 and not word.isnumeric()) or word in self.cnames: #or check if name in common list of words
                    names[n]=word
        return names,nums
    
    
    #this fuction takes the names dictionary from names fuction and joins these
    #names based on the position of then in text
    
    #this fuction returns a set of all joined names
    
    
    def fullnames(self,na):
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
    
 