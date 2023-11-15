def test_passing1():
    assert ('home', 'work') == ('home', 'work')


def test_passing2():
    assert ('QA') == ('QA')


def test_passing3():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)