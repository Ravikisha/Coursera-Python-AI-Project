import os
from machinetranslation import translator
def test_english_to_french():
    '''
    This function tests the english_to_french function
    '''
    assert translator.english_to_french('Hello') == 'Bonjour'

def test_french_to_english():
    '''
    This function tests the french_to_english function
    '''
    assert translator.french_to_english('Bonjour') == 'Hello'
    
if __name__ == "__main__":
    test_english_to_french()
    test_french_to_english()
    print("Everything passed")