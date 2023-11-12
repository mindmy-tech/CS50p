from seasons import minutesCalculator
import pytest

def test_init():

    test_case1 = minutesCalculator("2000-01-01")
    assert str(test_case1.dob) == "2000-01-01 00:00:00"



def test_sing():
    """"""
    test_case2 = minutesCalculator("2000-01-01")
    print(test_case2)
    assert (
        test_case2.__str__()
        == "Twelve million, four hundred sixty thousand, three hundred twenty minutes"
    )


def test_invalid_date():
    """"""
    with pytest.raises(ValueError):
        minutesCalculator("2000-13-13")
