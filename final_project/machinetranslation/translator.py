"""
This is how the lang coversion takes place
word_return = MyMemoryTranslator(source= ' ',target= ' ').translate(word)
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''
    instantiates the MyMemoryTranslator and uses the function translate
    to translate the text from en to fr
    '''
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''
    instantiates the MyMemoryTranslator and uses the function translate
    to translate the text from fr to en
    '''
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
    