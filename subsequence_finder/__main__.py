import argparse
import sys

from .subseq_finder import find_consecutive_runs


def main():
    input_array = [1, 2, 3, 4, 3, 2]
    result = find_consecutive_runs(input_array)

    print(result)

if __name__ == "__main__":
    sys.exit(main())
