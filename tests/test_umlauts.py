import pytest
from umlauts.umlauts import combination, convert_ascii_to_german


@pytest.mark.parametrize("haystack, needle, repl, pos, expected", [
    ("aa", "a", "b", 0, ["ab", "ba", "bb"]),
    ("aeae", "ae", "ä", 0, ['äae', 'ää', 'aeä']),
    ("aeaeae", "ae", "ä", 0, ['äaeae', 'ääae',
     'äää', 'äaeä', 'aeäae', 'aeää', 'aeaeä'])
])
def test_combination(haystack, needle, repl, pos, expected):
    assert set(combination(haystack, needle, repl, pos)) == set(expected)


# Test cases for convert_ascii_to_german function
@pytest.mark.parametrize("word, expected", [
    ("ae", ["ae", "ä"]),
    ("oe", ["oe", "ö"]),
    ("ue", ["ue", "ü"]),
    ("ss", ["ss", "ß"]),
    ("Ae", ["Ae", "Ä"]),
    ("Oe", ["Oe", "Ö"]),
    ("Ue", ["Ue", "Ü"]),
    ("SS", ["SS", "ß"]),
    ("AE", ["AE", "Ä"]),
    ("OE", ["OE", "Ö"]),
    ("UE", ["UE", "Ü"]),
    ("hallo", ["hallo"]),
    ("aeae", ['aeae', 'äae', 'ää', 'aeä']),
    ("aeaeae",  ['aeaeae', 'äaeae', 'ääae', 'äää', 'äaeä', 'aeäae', 'aeää', 'aeaeä']),
    ("aeoe", ['aeoe', 'äoe', 'aeö', 'äö']),
    ("aeoeue",  ['aeoeue', 'äoeue', 'aeöue', 'äöue', 'aeoeü', 'äoeü', 'aeöü', 'äöü']),
    ("aeoeae",  ['aeoeae', 'äoeae', 'äoeä', 'aeoeä', 'aeöae', 'äöae', 'äöä', 'aeöä']),
    ("strasse", ["strasse", "straße"]),
    ("Strasse", ["Strasse", "Straße"]),
    ("Strassen", ["Strassen", "Straßen"]),
    ("Strassens", ["Strassens", "Straßens"])
])
def test_convert_ascii_to_german(word, expected):
    assert set(convert_ascii_to_german(word)) == set(expected)
