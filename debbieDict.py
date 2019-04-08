

class DebbieDict(object):
    def __init__(self):
        greetings = self.generateGreetingDict()
        howru = self.generateHowAreYouDict()
        sorry = self.generateSorryDict()
        sad = self.generateThatsSadDict()
        self.dicts = [greetings, howru, sorry, sad]
        

    def getDicts(self):
        return self.dicts

    def generateThatsSadDict(self):
        inputs = ["sad", "sad.", "sad!", "bleak.", "bleak.", "bleak!", "awful.", "awful", "awful!", "terrible", "horrible.", "horrible!", "horrible"]
        responses = ["I guess it is.", "What isn't?", "I know.", "There's been worse.", "It could always be worse."]
        return [inputs, responses]

    def generateSorryDict(self):
        inputs = ["apologize", "apologize.", "apologize!", "sorry", "sorry.", "sorry!"]
        responses = ["apologies are meaningless.", "uh huh", "yup", "An apology is a good way to have the last word.", 
        "Sacrifice is at the heart of repentance. Without deeds, your apology is worthless.", "Forgiveness is the sweetest revenge.", 
        "Nothing wrong with apologizing, but saying I’m sorry does nothing when you continue to make the same mistakes..."]
        return [inputs, responses]

    def generateGreetingDict(self):
        inputs = ["hello", "hi", "greetings", "sup", "what's up","hey"]
        responses = ["hi", "hey", "*nods*", "yeah?",  "hi, I guess", "hello", "Hi. I guess we can talk. It's fine."]
        return [inputs, responses]

    def generateHowAreYouDict(self):
        inputs = ["how are you?", "how's it going?", "how are things?"]
        responses = ["fine", "idk, fine.", "I'd be better if the world wasn't falling apart around us.", "Fine... except. War. Cancer."]
        return [inputs, responses]