from um import count

def test_nrml():
    assert count("um") == 1
    assert count(" um?") == 1
def test_caps():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2