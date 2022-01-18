from msiaLex import modifier
def test_negation():
    assert modifier.disjunction('zh')

def test_intensifier():
    assert modifier.intensifier('zsm')
    
def test_disjunction():
    assert modifier.disjunction('en')

def test_stopword():
    assert modifier.stopword('en')
