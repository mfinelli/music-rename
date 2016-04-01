from music_rename import sanitize


def test_normal_string():
    assert sanitize.transliterate('abc') == 'abc'


def test_accented_characters():
    assert sanitize.transliterate('àâéèêëïîôùûüÿ') == 'aaeeeeiiouuuy'
