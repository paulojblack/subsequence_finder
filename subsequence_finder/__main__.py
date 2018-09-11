import sys

from .subseq_finder import find_consecutive_runs


def main():
    input_array = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
    result = find_consecutive_runs(input_array)

    print(result)

if __name__ == "__main__":
    sys.exit(main())
