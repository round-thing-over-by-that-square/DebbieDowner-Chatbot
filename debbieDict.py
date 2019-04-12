import random

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



    def generateResponseToQuestionType1(self):
        inputs = ["what", "is", "are", "how", "why", "when", "am", "was", "isnt", "wasnt", "were", "werent"]
        dismissive = ["I dont know but... ",
        "I have no idea.",
        "Ugh... That's so trivial in the grand scheme of things.",
        "I can't that right now.",
        "I wonder...",
        "So... anyhow...",
        "I can't say",
        ]
        nonsequiturs = self.generateNonSequiter()
        segway = self.generateSegway()
        return [inputs, random.choice(dismissive) + ". " + random.choice(segway) + random.choice(nonsequiturs)]


    def generateResponseToQuestionType2(self):
        inputs = ["will", "can", "did", "have", "should", "would", "could"]
        dismissive =  ["no.", "Nah", "Sure", "yeah", "yup", "nope", "Uh huh", "no", 
        "I have to think on it. Ask me again tomorrow.", "yes", "what do you think?"]
        nonsequiturs = self.generateNonSequiter()
        segway = self.generateSegway()
        return [inputs, random.choice(dismissive) + ". " + random.choice(segway) + random.choice(nonsequiturs)]

      
    def generateSegway(self):
        return ["Did you know that ",
        "Have you heard that ",
        "Can you believe that ",
        "Are you aware that ",
        "Isn't it crazy that "]
       
    def generateNonSequiter(self):   
        return ["The Spanish flu was the worst pandemic in history, killing 100 million people?",
        "One third of all homeless people in the United States are part of a homeless family?",
        "There are only 30000 rhinos left?",
        "A third of a mile long asteroid named Bennu might hit Earth on September 22, 2135?",
        "Lower respiratory infection is the most deadly communicable disease?",
        "the CDC estimates that between 12,000 and 56,000 flu-related deaths occur each year?",
        "People cut down 15 billion trees each year and the global tree count has fallen by 46 percent since the beginning of human civilization?",
        "In the U.S., youth homicide rates are more than 10 times that of other leading industrialized nations?",
        "More Americans have died from guns in the United States since 1968 than on battlefields of all the wars in American history?",
        "Passengers rode the stationary bicycles in the Gymnasium to pass time before the titanic sank?",
        "Over 1 million seabirds and 100,000 sea mammals are killed by pollution every year?",
        "The Mississippi River carries an estimated 1.5 million metric tons of nitrogen pollution into the Gulf of Mexico each year, creating a “dead zone” in the Gulf each summer about the size of New Jersey?",
        "Approximately 40 percent of the lakes in America are too polluted for fishing, aquatic life, or swimming?",
        "We dump 8.8 million tons of plastic into oceans every year?",
        "All tigers may become extinct in the wild within the next decade?",
        "Exposure to chlorine trifluoride will turn your bones to gelatin?"
        ]
        