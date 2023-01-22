from functions import *
#
# def test_add():
#     assert add(3, 5) == 8
#     assert add(120, 54) == 174
#
# def test_multiply():
#     assert multiply(100, 5) == 500
#     assert multiply(100, 1.1) == 110




def test_fissbuzz():
    assert fissbuzz(1) == 1
    assert fissbuzz(2) == 2
    assert fissbuzz(3) == 'fiss'
    assert fissbuzz(5) == 'buzz'
    assert fissbuzz(9) == 'fiss'
    assert fissbuzz(10) =='buzz'
    assert fissbuzz(15) == 'fissbuzz'
    assert fissbuzz(0) == 0
    assert fissbuzz(-5) == 0
    assert fissbuzz(4.4) == 4
    assert fissbuzz(4.51) == 'buzz'
    assert fissbuzz('mama') == 0