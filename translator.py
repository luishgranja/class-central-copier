from deep_translator import GoogleTranslator


class Translator:

    def __init__(self, glossary={}):
        self.glossary = glossary

    # translate: takes a string as input and returns its translation
    def translate(self, text: str):
        # search in dict for word in english
        # if it exists: use the value for that key
        if text in self.glossary:
            res = self.glossary[text]
        # if it does not exists: use the Google translator and save the translation
        else:
            res = GoogleTranslator(source='en', target='hi').translate(text=text)
            self.save_to_dictionary(text, res)
        return res

    # save_to_glossary: saves a key-value pair to the glossary
    def save_to_glossary(self, word, translation):
        self.glossary[word] = translation
