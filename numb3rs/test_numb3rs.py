from numb3rs import validate

def test_255():
    assert validate('255.255.255.255') == True

def test_275():
    assert validate('275.275.275.275') == False

def test_cat():
    assert validate('cat') == False

def test_first():
    assert validate('255.275.0.1') == False