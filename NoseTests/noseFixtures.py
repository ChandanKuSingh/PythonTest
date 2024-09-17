import nose

def test_addition():
    assert 1 + 1 == 3, "Expected 3, but got %d" % (1 + 1)

if __name__ == '__main__':
    nose.run(defaultTest=__name__)