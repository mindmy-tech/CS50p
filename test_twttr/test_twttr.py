from twttr import shorten
import pytest

def test_remove_sml_letter():
    assert shorten("sabari") == "sbr"
    assert shorten("aeiou") == ""

def test_remove_cap_letter():
    assert shorten("SABARI") == "SBR"
    assert shorten("AEIOU") == ""


def test_remove_mixed_letter():
    assert shorten("saBaRi") == "sBR"
    assert shorten("Shorten") == "Shrtn"

def test_numbers():
    assert shorten("1a2e3i4o5u6") == "123456"

def test_punc():
    assert shorten("sabari!") == "sbr!"

