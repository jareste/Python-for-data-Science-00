import sys
from ft_filter import ft_filter


def filter_words(s, n):
    assert isinstance(s, str) and isinstance(n, int), "the arguments are bad"
    return ft_filter(lambda word: len(word) > n, s.split())


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        s = sys.argv[1]
        n = int(sys.argv[2])
        result_ft_filter = filter_words(s, n)
        result_filter = list(filter(lambda word: len(word) > n, s.split()))
        print("Result from ft_filter: ", result_ft_filter)
        print("Result from    filter: ", result_filter)
    except AssertionError as e:
        print(e)
        sys.exit(1)
