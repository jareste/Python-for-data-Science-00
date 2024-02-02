import sys

def check_odd_even(number):
    assert isinstance(number, int), "Input must be an integer"
    if number % 2 == 0:
        print("I'm even")
    else:
        print("I'm odd")

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise AssertionError("You must provide exactly one argument")
    except AssertionError as e:
        print(e)
        sys.exit(1)
    assert len(sys.argv) == 2, "You must provide exactly one argument"
    try:
        num = int(sys.argv[1])
        check_odd_even(num)
    except ValueError:
        raise AssertionError("Input must be an integer")
