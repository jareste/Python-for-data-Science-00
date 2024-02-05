import sys


NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def encode_to_morse(s):
    assert isinstance(s, str) and all(c.isalnum() or c.isspace() for c in s), \
        "the arguments are bad"
    return ' '.join(NESTED_MORSE[c.upper()] for c in s)


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        s = sys.argv[1]
        print(encode_to_morse(s))
    except AssertionError as e:
        print(e)
        sys.exit(1)
