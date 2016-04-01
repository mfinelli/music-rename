from music_rename import sanitize

def test_good_string():
    assert sanitize.sanitize_final_character('abc') == 'abc'
