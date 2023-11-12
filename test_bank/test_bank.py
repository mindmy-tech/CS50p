from bank import value

def test_hello():
    assert value('hello') == 0

def test_h():
    assert value('hi') == 20

def test_greeting():
    assert value('goodbye') == 100

def test_upper():
    assert value('Hello') == 0