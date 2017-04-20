# Problem Set 4C
# Name: henrypj
# Collaborators: None
# Time Spent: x:xx

import string
import re
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
DEBUG = False

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words('words.txt')
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        transpose_dict = {}
        vowel_dict = {}

        i = 0
        for vowel in VOWELS_LOWER:
            vowel_dict[vowel] = vowels_permutation[i]
            i += 1

        i = 0
        for vowel in VOWELS_UPPER:
            vowel_dict[vowel] = vowels_permutation[i].upper()
            i += 1
        
        upper_lower = string.ascii_uppercase + string.ascii_lowercase
        i = 0
        for c in upper_lower:
            if c in VOWELS_LOWER + VOWELS_UPPER:
                transpose_dict[c] = vowel_dict[c]
            else:
                transpose_dict[c] = c

        return transpose_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_message = []
        if DEBUG:
            print("*** apply_transpose ***")
            print("  text to transpose => ", self.message_text)
            print("  transpose_dict => ", transpose_dict)
            
        for c in self.message_text:
            if c in string.ascii_lowercase + string.ascii_uppercase:
                encrypted_message.append(transpose_dict[c])
            else:
                encrypted_message.append(c)
        encrypted_message_str = ''.join(encrypted_message)
        if DEBUG:
            print("  transposed text => ", encrypted_message_str )
        return encrypted_message_str       

        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        if DEBUG:
            print("*** decrypt_message ***")
        vowel_perms = get_permutations(VOWELS_LOWER)
#        vowel_perms = ["eaiuo"]
        num_valid_words_max = 0
        for perm in vowel_perms:
            num_valid_words = 0
            test_message = SubMessage(self.message_text)
            if DEBUG:
                print("  perm => ", perm)
                print("  test_message1 => ", test_message.get_message_text())
            enc_dict = test_message.build_transpose_dict(perm)
            transposed_message = test_message.apply_transpose(enc_dict)
            if DEBUG:
                print("  test_message2 => ", transposed_message)
            
            for word in re.findall(r"[\w']+", transposed_message):
                if DEBUG:
                    print("  word => ", word)
                if is_word(self.valid_words, word):
                    if DEBUG:
                        print("  word is VALID")
                    num_valid_words += 1
#                else:
#                    print("  word is NOT VALID")
            
            if num_valid_words > num_valid_words_max:
                num_valid_words_max = num_valid_words
                valid_transposed_message = transposed_message
                if DEBUG:
                    print("  Decrypted_message => ", valid_transposed_message)

        if DEBUG:            
            print("  num_valid_words_max => ", num_valid_words_max)
            print("  Num of perms => ", x)
        if num_valid_words_max == 0:
            if DEBUG:
                print("  Returning... => ", self.message.text)
            return self.message_text
        else:
            if DEBUG:
                print("  Returning... => ", valid_transposed_message)
            return valid_transposed_message
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("=== ENCRYPTION TEST CASE ===")
    print("Original message:   ", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:  ", message.apply_transpose(enc_dict))
    
    print("=== DECRYPTION TEST CASE ===")
    print("Original message:   ", message.get_message_text())
    print("Expected decryption: Hello World!")
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Actual decryption:  ", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    message = SubMessage("Now is the time for all good men to come to the aid of their country.")
    permutation = "oueia"
    enc_dict = message.build_transpose_dict(permutation)
    print("=== ENCRYPTION TEST CASE ===")
    print("Original message:   ", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Niw es thu temu fir oll giid mun ti cimu ti thu oed if thuer ciantry.")
    print("Actual encryption:  ", message.apply_transpose(enc_dict))
    
    print("=== DECRYPTION TEST CASE ===")
    print("Original message:   ", message.get_message_text())
    print("Expected decryption: Now is the time for all good men to come to the aid of their country.", )
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Actual decryption:  ", enc_message.decrypt_message())
    
    
