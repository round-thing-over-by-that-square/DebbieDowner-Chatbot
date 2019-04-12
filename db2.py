from debbieDict import DebbieDict

import nltk
import warnings
warnings.filterwarnings("ignore")

# nltk.download() # for downloading packages
import numpy as np
import random

import string # to process standard python strings
from string import punctuation




data = open("chatData.txt", "a+")
f=open('debbie.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()# converts to lowercase
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only
phrases = [p for p in raw.split('\n') if p]
sent_tokens = []
dictionary = DebbieDict()
historicPhrases = [[],[]] #stores all phrases from converstaion, input in [0] and responses in [1]
for p in phrases:
    sent_tokens.append(p)
word_tokens = nltk.word_tokenize(raw)# converts to list of words

sent_tokens[:2]

word_tokens[:5]


lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# check for exact match with given phrase
def checkPhrase(sentence, dictionary, row, col):
    for phrase in dictionary.dicts[row][col]: 
        if sentence == phrase: 
            return random.choice(dictionary.dicts[row][col+1]) 

# Checking for match with given word
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
        userResponseTokens = nltk.word_tokenize(user_response)# converts to list of words
        debresponse1 = dictionary.generateResponseToQuestionType1()[0]
        for word in debresponse1:
            if userResponseTokens[0] == word:
                robo_response = dictionary.generateResponseToQuestionType1()[1]
        if robo_response == '':
            debresponse2 = dictionary.generateResponseToQuestionType2()[0]
            for w in debresponse2:
                if userResponseTokens[0] == w:
                    robo_response = dictionary.generateResponseToQuestionType2()[1]
        if robo_response == '':
            robo_response=robo_response+random.choice(responses)
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


flag=True
print("Debbie: My name is Debbie. I am here to talk. If you want to exit, type Bye")


while(flag==True):
    user_response = input()
    data.write("User: " + user_response + "\n") 
    user_response=user_response.lower()
    historicPhrases[0].append(user_response) 
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Debbie: You are welcome..")
        else:
            #check for greeting
            if(checkWord(user_response, dictionary, 0, 0)!=None):
                response1 = checkWord(user_response, dictionary, 0, 0)
                historicPhrases[1].append(response1) 
                print("Debbie: " + response1)
            #check "how are you?" and related questions    
            elif(checkPhrase(user_response, dictionary, 1, 0)!=None): 
                response1 = checkPhrase(user_response, dictionary, 1, 0)
                historicPhrases[1].append(response1) 
                print("Debbie: "+ response1)
            #check for apologies
            elif(checkWord(user_response, dictionary, 2, 0)!=None):
                response1 = checkWord(user_response, dictionary, 2, 0)
                historicPhrases[1].append(response1) 
                print("Debbie: "+ response1)
            #check for "that's sad." and such
            elif(checkWord(user_response, dictionary, 3, 0)!=None):
                response1 = checkWord(user_response, dictionary, 3, 0)
                historicPhrases[1].append(response1) 
                print("Debbie: "+ response1)
            #check for what's up
            elif(checkPhrase(user_response, dictionary, 4, 0)!=None): 
                response1 = checkPhrase(user_response, dictionary, 4, 0)
                historicPhrases[1].append(response1) 
                print("Debbie: "+ response1)
            else:
                print("Debbie: ",end="")
                response1 = response(user_response)
                print(response1)
                historicPhrases[1].append(response1) 
                sent_tokens.remove(user_response)
            data.write("Debbie: " + response1 + "\n")
    else:
        flag=False
        print("Debbie: Bye! take care..")   
        print(historicPhrases) 
