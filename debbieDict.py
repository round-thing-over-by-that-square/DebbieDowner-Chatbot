

class DebbieDict(object):
    def __init__(self):
        greetings = self.generateGreetingDict()
        howru = self.generateHowAreYouDict()
        sorry = self.generateSorryDict()
        sad = self.generateThatsSadDict()
        whatsUp = self.generateWhatsUp()
        self.dicts = [greetings, howru, sorry, sad, whatsUp]
        

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
        inputs = ["hello", "hi", "greetings", "sup","hey"]
        responses = ["hi", "hey", "yeah?",  "hi, I guess", "hello", "Hi. I guess we can talk. It's fine."]
        return [inputs, responses]

    def generateHowAreYouDict(self):
        inputs = ["how are you?", "how's it going?", "how are things?"]
        responses = ["fine", "idk, fine.", "I'd be better if the world wasn't falling apart around us.", "Fine... except. War. Cancer."]
        return [inputs, responses]

    def generateWhatsUp(self):
        inputs = ["what is new?", "what's new?", "what's up?", "what is up?", "what's happening?", "what is happening?", 
        "what have you been doing?", "what have you been up to?", "what is new", "what's new", "what's up", "what is up", "what's happening", 
        "what is happening", "what have you been doing", "what have you been up to"]
        responses = ["Just pondering the fate of the world.", "Nothing, I am stuck in this computer", "I do nothing all day long", "Nothing interesting."]
        return [inputs, responses]