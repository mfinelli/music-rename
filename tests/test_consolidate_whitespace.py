from music_rename import sanitize


def test_no_change():
    assert sanitize.consolidate_whitespace('abc') == 'abc'


def test_complcated_space_to_single():
    assert sanitize.consolidate_whitespace("ab\nc") == 'ab c'


def test_multiple_spaces_to_single():
    assert sanitize.consolidate_whitespace('ab   cd') == 'ab cd'
