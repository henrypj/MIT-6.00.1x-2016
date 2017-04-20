# Problem Set 2, hangman.py
# Name: henrypj
# Collaborators: None
# Time spent: 

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import sys
VERSION = int(sys.version_info[0])
if VERSION >= 3:
    raw_input = input

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def num_unique_letters(secret_word):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are lowercase
    returns: integer, the number of unique letters in secret_word
    '''
    unique_letters = ''
    for c in secret_word:
        if not c in unique_letters:
            unique_letters += c
    return len(unique_letters)



def is_letter_guessed(letter, secret_word, letters_guessed):
    '''
    letter: string, current letter of secret_word being tested to see if in
      letters_guessed
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if letter is in letters_guessed, False otherwise
    '''
    if letter in secret_word:
        print("Good guess: " + str(get_guessed_word(secret_word, letters_guessed)))
        return True
    else:
        print("Oops! That letter is not in my word: " + str(get_guessed_word(secret_word, letters_guessed)))
        return False



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for c in secret_word:
        if not c in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ''
    good_guess = False

    for c in secret_word:
        if c in letters_guessed:
            guessed_word += c
        else:
            guessed_word += "_ "

    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    available_letters = ''

    for c in string.ascii_lowercase:
        if not c in letters_guessed:
            available_letters += c
    return available_letters
    


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    x = 0
    num_guesses = 6
    warnings = 3
    letters_guessed = ''
    #vowels = ['a', 'e', 'i', 'o', 'u']
    vowels = 'aeiou'
    word_len = str(len(secret_word))

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + word_len + " letters long.")
    print("---------------")

    print("You have " + str(num_guesses) + " guesses left.")
    print("Available letters: " + get_available_letters(letters_guessed))

    while x <= num_guesses:
        guessed_word = ''
        good_guess = False

        guess = raw_input("Please guess a letter: ").lower()

        while not guess.isalpha() or len(guess) > 1:
            warnings -= 1
            if warnings <= 0:
                warnings = 0
                print("Warnings exceeded, reducing # of guesses by 1.")
                break
            print("Invalid input, only single characters allowed. Please try again.")
            print("You have " + str(warnings) + " warnings left.")
            print("You have " + str(num_guesses - x) + " guesses left.")
            print("Available letters: " + get_available_letters(letters_guessed))
            guess = raw_input("Please guess a letter: ").lower()
        
        if guess in letters_guessed:
            print("You have already guessed that letter.")
            if warnings >= 1:
                warnings -= 1
                print("Incrementing Warnings by +1")
            if warnings == 0:
                x += 1
                print("Incrementing # of guesses by +1")
        else:
            letters_guessed += guess
            good_guess = is_letter_guessed(guess, secret_word, letters_guessed)

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            total_score = (num_guesses - x) * num_unique_letters(secret_word)
            print("Your total score for this game is: " + str(total_score))
            break
        else:
            get_guessed_word(secret_word, letters_guessed)

            if not good_guess:
                x += 1

                # If guess is a vowel, player loses another guess
                if guess in vowels:
                    print("Letter is a vowel, lose 2 guesses.")
                    x += 1

            if x == num_guesses:
                print("Guesses exhausted. You lose!")
                print("The secret word was: " + secret_word)
                break

            print("---------------")
            print("You have " + str(warnings) + " warnings left.")
            print("You have " + str(num_guesses - x) + " guesses left.")
            print("Available letters: " + get_available_letters(letters_guessed))

# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new_word = ""
    letters_revealed = ""

    for char in my_word: new_word = my_word.replace(" ","")

    for char in new_word:
        if char != "_":
            letters_revealed += char

    if len(new_word) != len(other_word):
        return False

    for i in range(0, len(new_word)):
        if new_word[i] != other_word[i] and new_word[i] != "_":
            return False
        if new_word[i] == "_" and other_word[i] in letters_revealed:
            return False

    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    matches_found = False
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches_found = True
            print (word,)
    
    if not matches_found:
        print ("No matches found")
    else:
        print ('\n')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    x = 0
    num_guesses = 6
    warnings = 3
    letters_guessed = ''
    guessed_word = ''
    #vowels = ['a', 'e', 'i', 'o', 'u']
    vowels = 'aeiou'
    word_len = str(len(secret_word))

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + word_len + " letters long.")
    print("---------------")

    print("You have " + str(num_guesses) + " guesses left.")
    print("Available letters: " + get_available_letters(letters_guessed))

    while x <= num_guesses:
        good_guess = False

        guess = raw_input("Please guess a letter: ").lower()

        while (not guess.isalpha() or len(guess) > 1) and guess != "*":
            warnings -= 1
            if warnings <= 0:
                warnings = 0
                print("Warnings exceeded, reducing # of guesses by 1.")
                break
            print("Invalid input, only single alpha characters or * allowed. Please try again.")
            print("You have " + str(warnings) + " warnings left.")
            print("You have " + str(num_guesses - x) + " guesses left.")
            print("Available letters: " + get_available_letters(letters_guessed))
            guess = raw_input("Please guess a letter: ").lower()

        if guess == "*":
            print("Possible matches are:")
            show_possible_matches(guessed_word)

        else:
            if guess in letters_guessed:
                print("You have already guessed that letter.")
                if warnings >= 1:
                    warnings -= 1
                    print("Incrementing Warnings by +1")
                if warnings == 0:
                    x += 1
                    print("Incrementing # of guesses by +1")
            else:
                letters_guessed += guess
                good_guess = is_letter_guessed(guess, secret_word, letters_guessed)

            if is_word_guessed(secret_word, letters_guessed):
                print("Congratulations, you won!")
                total_score = (num_guesses - x) * num_unique_letters(secret_word)
                print("Your total score for this game is: " + str(total_score))
                break
            else:
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                        
                if not good_guess:
                    x += 1
  
                    # If guess is a vowel, player loses another guess
                    if guess in vowels:
                        print("Letter is a vowel, lose 2 guesses.")
                        x += 1

                if x == num_guesses:
                    print("Guesses exhausted. You lose!")
                    print("The secret word was: " + secret_word)
                    break
  
                print("---------------")
                print("You have " + str(warnings) + " warnings left.")
                print("You have " + str(num_guesses - x) + " guesses left.")
                print("Available letters: " + get_available_letters(letters_guessed))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    #secret_word = "apple"
    #hangman(secret_word)
    #secret_word = "dolphin"
    #hangman(secret_word)
    #wordlist = ["e", "i", "k", "p", "r", "s"]
    #print(is_word_guessed(secret_word, wordlist))
    #print(get_guessed_word(secret_word, wordlist))
    #print(get_available_letters(wordlist))

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    
    #secret_word = 'tact'
    #hangman_with_hints(secret_word)
    #print(match_with_gaps("te_ t", "tact"))
    #print(match_with_gaps("a_ _ le", "banana"))
    #print(match_with_gaps("a_ _ le", "apple"))
    #print(match_with_gaps("a_ ple", "apple"))
    #show_possible_matches("t_ _ t")
    #show_possible_matches("a_ _ le")
    #show_possible_matches("aaabc_ _")
