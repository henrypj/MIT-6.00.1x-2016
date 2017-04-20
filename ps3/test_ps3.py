from ps3 import *

#
# Test code
#

def test_deal_hand():
    """
    Unit test for deal_hand
    """
    failure=False
    num_hands = 10
    num_wildcards = 0
    
    for i in range(0,num_hands):
        hand = deal_hand(i)
        
        if WILDCARD in hand:
            num_wildcards += 1
            
    if num_wildcards != (num_hands - 1):
        print("FAILURE: test_deal_hand()")
        print("\tExpected " + str(num_hands) + " wildcards, but only found " + str(num_wildcards))
        failure=True

    if not failure:
        print("SUCCESS: test_deal_hand()")

# end of test_deal_hand


def test_calculate_handlen():
    """
    Unit test for calculate_handlen
    """
    failure=False

    # test 1
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    handlen = calculate_handlen(hand)
    
    if handlen != 7:
        print("FAILURE: test_calculate_handlen()")
        print("\tExpected 7, but got " + str(handlen) + " for hand:", hand)
        failure = True

    # test 2
    hand = {'a': 1, 'r': 2, '*': 1, 'z': 0, 'm': 1, 'q': 1}
    handlen = calculate_handlen(hand)
    
    if handlen != 6:
        print("FAILURE: test_calculate_handlen()")
        print("\tExpected 6, but got " + str(handlen) + " for hand:", hand)
        failure = True
    
    if not failure:
        print("SUCCESS: test_calculate_handlen()")
        
# end of test_calculate_handlen


def test_play_hand():
    """
    Unit test for play_hand
    """
    failure=False

    # test 1
    # test with "jar" as first word and "f*x" as second  
    hand = {'a': 1, 'j': 1, 'e': 1, 'f': 1, '*': 1, 'r': 1, 'x': 1}
    
    score = play_hand(hand, word_list)
    if score != 306:
        print("FAILURE: test_play_hand()")
        print("\tExpected 306, but got " + str(score) + " for word: " + word)
        failure = True
    
    # test 2
    # test with "fix" as first word, "ac" as second and "*t" as third  
    hand = {'a': 1, 'c': 1, 'f': 1, 'i': 1, '*': 1, 't': 1, 'x': 1}
    
    score = play_hand(hand, word_list)
    if score != 131:
        print("FAILURE: test_play_hand()")
        print("\tExpected 131, but got " + str(score) + " for word: " + word)
        failure = True

    if not failure:
        print("SUCCESS: test_play_hand()")

# end of test_play_hand


def test_substitute_hand():
    """
    Unit test for substitute_hand
    """
    failure=False

    # test 1
    hand = {'h':1, 'e':1, 'l':2, 'o':1}
    letter = 'l'
    
    new_hand = substitute_hand(hand, letter)
    print("new_hand => ", new_hand)
    if letter in new_hand:
        print("FAILURE: test_substitute_hand()")
        print("\tExpected letter \'l\' to be replaced in new_hand: ", new_hand)
        failure = True

    # test 2
    hand = {'a': 1, 'j': 1, 'e': 1, 'f': 1, '*': 1, 'r': 1, 'x': 1}
    letter = 'j'
    
    new_hand = substitute_hand(hand, letter)
    print("new_hand => ", new_hand)
    if letter in new_hand:
        print("FAILURE: test_substitute_hand()")
        print("\tExpected letter \'j\' to be replaced in new_hand: ", new_hand)
        failure = True

    if not failure:
        print("SUCCESS: test_substitute_hand()")
    
# end of test_substitute_hand


def test_get_word_score():
    """
    Unit test for get_word_score
    """
    failure=False
    # dictionary of words and scores
    words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
             ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
             ("fork", 7):209, ("FORK", 4):308, ("jar", 7): 90, 
             ("f*x", 4):216}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score()")
            print("\tExpected", words[(word, n)], "points but got '" + \
                  str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True
    if not failure:
        print("SUCCESS: test_get_word_score()")

# end of test_get_word_score


def test_update_hand():
    """
    Unit test for update_hand
    """
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {'l':1, 'm':1}
    expected_hand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        return # exit function
    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function
        
    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "Evil"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {'v':1, 'n':1, 'l':1}
    expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")        
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "HELLO"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {}
    expected_hand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")                
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)
        
        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function

    print("SUCCESS: test_update_hand()")

# end of test_update_hand

def test_is_valid_word(word_list):
    """
    Unit test for is_valid_word
    """
    failure=False
    # test 1
    word = "hello"
    handOrig = get_frequency_dict(word)
    handCopy = handOrig.copy()

    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", handOrig)

        failure = True

    # Test a second time to see if word_list or hand has been modified
    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")

        if handCopy != handOrig:
            print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
            print("\tAt this point, hand ought to be", handOrig, "but it is", handCopy)

        else:
            print("\tTesting word", word, "for a second time - have you modified word_list?")
            wordInWL = word in word_list
            print("The word", word, "should be in word_list - is it?", wordInWL)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", handCopy)

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "Rapture"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True        

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True                        

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        
        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "EVIL"
    
    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)
        
        failure = True
        
    # test 6
    word = "Even"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)")        
        
        failure = True        

    # test 7
    hand = {'e':1, 'v':1, 'z':1, 'n':1, 'i':1, 'l':2}
    word = "ezen"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, check to make sure is_valid_word() is checking that the word is in the word_list.")

    # test 8
    hand = {'a':1, 'c':1, 'f': 1, 'i':1, '*':1, 't':1, 'x':1}
    word = "ac"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, check to make sure is_valid_word() is checking that the word is in the word_list.")

    if not failure:
        print("SUCCESS: test_is_valid_word()")
        
    
    

# end of test_is_valid_word

def test_wildcard(word_list):
    """
    Unit test for is_valid_word
    """
    failure=False

    # test 1
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    word = "e*m"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 2
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 3
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "h*ney"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 4
    hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
    word = "c*wz"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '"+ word +"' and hand:", hand)

        failure = True    

    # dictionary of words and scores WITH wildcards
    words = {("h*ney", 7):290, ("c*ws", 6):176, ("wa*ls", 7):203}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score() with wildcards")
            print("\tExpected", words[(word, n)], "points but got '" + \
                  str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True      

    if not failure:
        print("SUCCESS: test_wildcard()")


word_list = load_words()
print("----------------------------------------------------------------------")
print("Testing deal_hand...")
test_deal_hand()
print("----------------------------------------------------------------------")
print("Testing get_word_score...")
test_get_word_score()
print("----------------------------------------------------------------------")
print("Testing update_hand...")
test_update_hand()
print("----------------------------------------------------------------------")
print("Testing is_valid_word...")
test_is_valid_word(word_list)
print("----------------------------------------------------------------------")
print("Testing wildcards...")
test_wildcard(word_list)
print("----------------------------------------------------------------------")
print("Testing calculate_handlen...")
test_calculate_handlen()
print("----------------------------------------------------------------------")
print("Testing play_hand...")
test_play_hand()
print("----------------------------------------------------------------------")
print("Testing substitute_hand...")
test_substitute_hand()
print("All done!")
