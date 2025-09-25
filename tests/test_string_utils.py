from scripts import string_utils as su


def test_normalize_whitespace():
    assert su.normalize_whitespace("  a   b\n c\t") == "a b c"


def test_word_frequencies():
    text = "Apple apple's APPLE, banana."
    freq = su.word_frequencies(text)
    assert freq["apple"] == 3  # apple, apple's, APPLE
    assert freq["banana"] == 1


def test_is_palindrome():
    assert su.is_palindrome("Madam, I'm Adam")
    assert not su.is_palindrome("Hello")
