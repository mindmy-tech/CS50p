from fuel import convert, gauge
import pytest

def test_1():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_2():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(25) == "25%"
    assert gauge(99) == "F"

def test_dividezero():
    with pytest.raises(ZeroDivisionError):
        convert('100/0')

def test_alphabet():
    with pytest.raises(ValueError):
        convert('a/b')
