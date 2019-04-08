

class DebbieDict(object):
    def __init__(self):
        self.greetings = self.generateGreetingDict()
        self.howru = self.generateHowAreYouDict()
        self.dicts = [self.greetings, self.howru]
        

    def getDicts(self):
        return self.dicts

    def generateGreetingDict(self):
        inputs = ["hello", "hi", "greetings", "sup", "what's up","hey"]
        responses = ["hi", "hey", "*nods*", "yeah?",  "hi, I guess", "hello", "Hi. I guess we can talk. It's fine."]
        return [inputs, responses]

    def generateHowAreYouDict(self):
        inputs = ["how are you?", "how's it going?", "how are things?"]
        responses = ["fine", "idk, fine.", "I'd be better if the world wasn't falling apart around us.", "Fine... except. War. Cancer."]
        return [inputs, responses]