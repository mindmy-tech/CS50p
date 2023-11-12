from jar import Jar
import pytest

def test_init():
    test_jar_1 = Jar()
    assert test_jar_1.capacity == 12
    test_jar_2 = Jar(15)
    assert test_jar_2.capacity == 15
    assert test_jar_1.size == 0

def test_negative_capacity():
    with pytest.raises(ValueError):
        Jar(-10)


def test_underflow_cookies():
    with pytest.raises(ValueError):
        test_jar_1 = Jar()
        test_jar_1.withdraw(1)

def test_overflow_cookies():
    with pytest.raises(ValueError):
        test_jar_1 = Jar()
        test_jar_1.deposit(13)

