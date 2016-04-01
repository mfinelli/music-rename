from music_rename import sanitize


def test_normal_string():
    assert sanitize.transliterate('abc') == 'abc'


def test_accented_characters():
    assert sanitize.transliterate('àâéèêëïîôùûüÿ') == 'aaeeeeiiouuuy'


def test_more_complicated_characters():
    assert sanitize.transliterate('æœß') == 'aeoess'


def test_symbols():
    assert sanitize.transliterate('’“”«»–…') == '\'""<<>>-...'


def test_unchanged():
    assert sanitize.transliterate('$%#') == '$%#'
