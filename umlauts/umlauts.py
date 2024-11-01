

def combination(haystack, needle, repl, pos):
    lst = []
    start = haystack.find(needle, pos)
    if 0 <= start:
        replaced = haystack[:start] + repl + haystack[start + len(needle):]
        if start+len(repl) < len(haystack):
            lst.extend(combination(replaced, needle, repl, start+len(repl)))
            lst.extend(combination(haystack, needle, repl, start+len(repl)))
    else:
        lst.append(haystack)
    return lst


def convert_ascii_to_german(word):
    """
    Converts ASCII digraphs (ae, oe, ue, ss) in a German word to umlauts and eszett,
    handling uppercase and capitalized words correctly.

    Args:
        word: The German word as a string.

    Returns:
        The converted word with umlauts and eszett.
    """

    combinations = [word]  # Start with the original word

    replacements = {
        "ae": "ä",
        "oe": "ö",
        "ue": "ü",
        "ss": "ß",
        "Ae": "Ä",
        "Oe": "Ö",
        "Ue": "Ü",
        "Ss": "ß",
        "AE": "Ä",
        "OE": "Ö",
        "UE": "Ü",
        "SS": "ß"
    }

    for char, replacement in replacements.items():
        new_combinations = []
        for combo in combinations:
            if char in combo:
                new_combinations.extend(
                    combination(combo, char, replacement, 0))
                new_combinations.remove(combo)
        combinations.extend(new_combinations)

    return list(combinations)  # Remove duplicates


# Example usage
word = "aeaeoe"
converted_word = convert_ascii_to_german(word)
print(f"Conversion of '{word}': {converted_word}")

word = "Gruesse"
converted_word = convert_ascii_to_german(word)
print(f"Conversion of '{word}': {converted_word}")

word = "aether"
converted_word = convert_ascii_to_german(word)
print(f"Conversion of '{word}': {converted_word}")

word = "GROESSE"
converted_word = convert_ascii_to_german(word)
print(f"Conversion of '{word}': {converted_word}")
