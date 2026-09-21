def somme(a, b) : return a+b

def test_somme():
    assert somme(5,6) == 11
    assert somme(-5, 5) == 0
    assert somme(0, 8) == 8

def soustrait(a,b) : return a-b

def test_soustrait() :
    assert soustrait(5,1) == 4
    assert soustrait(10, 20) == -10