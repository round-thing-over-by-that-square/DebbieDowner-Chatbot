#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only

from debbieDict import DebbieDict

import nltk
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import random

import string # to process standard python strings
from string import punctuation





f=open('debbie.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()# converts to lowercase
phrases = [p for p in raw.split('\n') if p]
sent_tokens = []
for p in phrases:
    sent_tokens.append(p)
word_tokens = nltk.word_tokenize(raw)# converts to list of words
#for file_id in reuters.fileids():
#    word_tokens.append(set(nltk.word_tokenize(reuters.raw(file_id))))

#print(word_tokens)

sent_tokens[:2]

word_tokens[:5]


lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


#check for "how are you?"
def checkPhrase(sentence, dictionary, row, col):
    for phrase in dictionary.dicts[row][col]: 
        if sentence == phrase: #  getDicts()[1][1]) #HOW_ARE_YOU_OUT)
            return random.choice(dictionary.dicts[row][col+1]) 

# Checking for greetings
def checkWord(sentence, dictionary, row, col):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in dictionary.dicts[row][col]: 
            return random.choice(dictionary.dicts[row][col+1]) 


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Generating response
def response(user_response):
    responses = ["I'm not sure I understand.",
     "Please go on.",
     "What does that suggest to you?",
     "Do you feel strongly about discussing such things?",
     "That is interesting.  Please continue.",
     "Uh huh, go on.",
     "Tell me more about that.",
     "I am sorry! I don't understand you"]
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+random.choice(responses)
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


flag=True
print("Debbie: My name is Debbie. I am here for you to talk at. If you want to exit, type Bye")
dictionary = DebbieDict()
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Debbie: You are welcome..")
        else:
            #check for greeting
            if(checkWord(user_response, dictionary, 0, 0)!=None):
                print("Debbie: "+checkWord(user_response, dictionary, 0, 0))
            #check "how are you?" and related questions    
            elif(checkPhrase(user_response, dictionary, 1, 0)!=None): 
                print("Debbie: "+checkPhrase(user_response, dictionary, 1, 0))
            else:
                print("Debbie: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Debbie: Bye! take care..")    