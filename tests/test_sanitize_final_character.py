from music_rename import sanitize


def test_good_string():
    assert sanitize.sanitize_final_character('abc') == 'abc'


def test_remove_illegal_final_character():
    assert sanitize.sanitize_final_character('abc abd(') == 'abc abd'


def test_remove_trailing_whitespace():
    assert sanitize.sanitize_final_character('abc   ') == 'abc'


def test_remove_initial_whitespace():
    assert sanitize.sanitize_final_character('   abc') == 'abc'


def test_multiple_remove_rounds():
    assert sanitize.sanitize_final_character('abc&&&&') == 'abc'


def test_multipe_remove_whitespace_rounds():
    assert sanitize.sanitize_final_character('abc [ [') == 'abc'


def test_leave_middle_characters_alone():
    assert sanitize.sanitize_final_character('abc \' abc') == 'abc \' abc'


def test_remove_trailing_dash():
    assert sanitize.sanitize_final_character('abc-') == 'abc'
