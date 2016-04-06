from music_rename import sanitize


def test_no_change():
    assert sanitize.remove_dash_space('abc') == 'abc'


def test_dash_middle():
    assert sanitize.remove_dash_space('ab-cd') == 'ab-cd'


def test_remove_dash_space():
    assert sanitize.remove_dash_space('ab- cd') == 'ab cd'


def test_beginning_dash():
    assert sanitize.remove_dash_space('-abc') == '-abc'


def test_ending_dash():
    assert sanitize.remove_dash_space('abc-') == 'abc-'
