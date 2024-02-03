import sys
import string


def count_chars(text):
    upper_letters = sum(c.isupper() for c in text)
    lower_letters = sum(c.islower() for c in text)
    punctuation_marks = sum(c in string.punctuation for c in text)
    spaces = text.count(' ')
    digits = sum(c.isdigit() for c in text)
    return upper_letters, lower_letters, punctuation_marks, spaces, digits


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        text = input("Please provide a string: ")
    elif len(args) > 1:
        raise AssertionError("Only one argument is allowed")
    else:
        text = args[0]
    upper_letters, lower_letters, punctuation_marks, spaces, \
        digits = count_chars(text)
    print(f"The text contains {len(text)} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{punctuation_marks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)
        sys.exit(1)
