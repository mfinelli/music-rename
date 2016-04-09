from music_rename import sanitize

def test_no_change():
    assert sanitize.sanitize('abc', 10) == 'abc'

def test_truncate():
    assert sanitize.sanitize('abcdef', 3) == 'abc'

def test_no_trailing_dash():
    assert sanitize.sanitize('abc-', 10) == 'abc'


def test_remove_illegal_characters():
    assert sanitize.sanitize('ab * * cd', 5) == 'ab cd'


def test_accented_characters():
    assert sanitize.sanitize('àbcdë', 5) == 'abcde'


def test_beginning_parenthesis():
    assert sanitize.sanitize('abc()', 4) == 'abc'


def test_ending_parenthesis():
    assert sanitize.sanitize('abc()', 5) == 'abc()'
