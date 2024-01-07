from project import *


def test_is_valid_word():
    assert is_valid_word("hello") == True
    assert is_valid_word("xylophone") == True
    assert is_valid_word("qwerty") == False
    assert is_valid_word("123") == False

def test_get_random_word():
    wordsize = 5
    word = get_random_word(wordsize)
    assert len(word) == wordsize
    assert is_valid_word(word)

def test_check_word():
    word = "apple"
    guess = "paler"
    wordsize = len(word)
    status = [0 for i in range(wordsize)]
    result = check_word(guess, wordsize, status, word)
    assert result == [1, 1, 1, 1, 0]

