import unittest
import random

### Takes in an array of unsorted integers and a desired length
### of subsequence
def find_consecutive_runs(raw_array, subseq_length=3):
    neg_sequence_counter = 0
    pos_sequence_counter = 0
    consecutive_neg = [0]
    consecutive_pos = [0]

    subsequence_start_idxs = []

    for idx in range(1, len(raw_array)):
        current_elem = raw_array[idx]
        prev_elem = raw_array[idx-1]

        if current_elem - 1 == prev_elem:
            pos_sequence_counter += 1
        else:
            pos_sequence_counter = 0
            subsequence_start_idxs += sub_sequence_reset(consecutive_pos, subseq_length)
            consecutive_pos = []

        if current_elem + 1 == prev_elem:
            neg_sequence_counter += 1
        else:
            neg_sequence_counter = 0
            subsequence_start_idxs += sub_sequence_reset(consecutive_neg, subseq_length)
            consecutive_neg = []

        consecutive_pos.append(idx)
        consecutive_neg.append(idx)
        
    # Lazy catch for the case where a list ends during a subsequence
    subsequence_start_idxs += sub_sequence_reset(consecutive_pos)
    subsequence_start_idxs += sub_sequence_reset(consecutive_neg)

    return subsequence_start_idxs


### Each index up until the final two can be considered
### the first index of a consecutive subsequence of length 3
def sub_sequence_reset(consecutive_idxs, subseq_length=3):
    consecutive_idx_offset = 1 - subseq_length

    subsequence_start_idxs = consecutive_idxs[:consecutive_idx_offset]

    return subsequence_start_idxs


