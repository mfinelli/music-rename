from music_rename import sanitize


def test_no_change():
    assert sanitize.remove_unrecognized_characters('abc') == 'abc'


def test_remove_many():
    assert sanitize.remove_unrecognized_characters('ab{}*^$# !a') == 'ab a'
