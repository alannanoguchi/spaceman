from spaceman import is_guess_in_word, is_word_guessed, get_guessed_word
import pytest


def test_is_guess_in_word():
    assert is_guess_in_word("r", "read") == True
    assert is_guess_in_word("x", "read") == False

def test_is_word_guessed():
    assert is_word_guessed("read", "read") == True
    assert is_word_guessed("read", "reed") == False

def test_get_guessed_word():
    assert get_guessed_word("read", "breed") == False
    assert get_guessed_word("read", "read") == True

  


# run the tests
if '__name__' == '__main__':
    test_is_word_guessed()
    test_is_guess_in_word()
    test_get_guessed_word()