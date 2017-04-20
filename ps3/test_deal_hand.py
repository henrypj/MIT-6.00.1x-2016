from ps3 import *

def test_deal_hand():
    """
    Unit test for deal_hand
    """
    failure=False
    for i in range(1,7):
        hand = deal_hand(i)
        print(hand)
    # dictionary of words and scores
#    words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
#             ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
#             ("fork", 7):209, ("FORK", 4):308}
#    for (word, n) in words.keys():
#        score = get_word_score(word, n)
#        if score != words[(word, n)]:
#            print("FAILURE: test_get_word_score()")
#            print("\tExpected", words[(word, n)], "points but got '" + \
#                  str(score) + "' for word '" + word + "', n=" + str(n))
#            failure=True
    if not failure:
        print("SUCCESS: test_deal_hand()")

# end of test_get_word_score

