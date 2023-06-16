import pytest

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    sorted_word1 = sorted(word1.lower())
    sorted_word2 = sorted(word2.lower())
    return sorted_word1 == sorted_word2

def test_is_anagram():
    assert is_anagram("listen", "silent") == True

    assert is_anagram("heart", "earth") == True

    assert is_anagram("Torch", "rotch") == True

    assert is_anagram("debit", "bed") == False

    assert is_anagram("hello", "world") == False

    assert is_anagram("debit card", "bad credit") == False
