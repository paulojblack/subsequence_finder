# subsequence_finder

A simple python project to find which indices in an input array of integers are the first element in a subsequence of length 3 consisting of numbers consecutively increasing or decreasing by 1

For example, an input of [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7] will return [0, 4, 6, 7]

All inputs are hardcoded currently, so to alter the input array, simply edit the `input_array` variable in `subequence_finder/__main__.py`.

The solution was created to solve for subsequences of length 3, but it seems pretty easy to generalize the solution to subsequences of any length, and so I've included as an additional input parameter a `subseq_length` variable which defaults to 3. That's only been manually tested for a few cases and I'm sure it'll bug out at some edge cases.

## Setup
No setup necessary.

## Execution
From the project root directory run  
python -m subsequence_finder

## Testing
A simple file with a couple tests used in development is located in `tests/test_subsequences`  

To execute, from the project root directory run  
`python -m unittest discover -s ./tests/`