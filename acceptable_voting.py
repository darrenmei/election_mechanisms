import numpy as np
import pandas as pd
import sys

from preprocess_data import *

def compute_votes(data):
    sum_acceptable_votes = np.zeros(8)

    for i in range(len(data)):
        last_acceptable_candidate = data[i][6]
        if last_acceptable_candidate > 0:
            ranked_list = data[i][5]
            for j in range(last_acceptable_candidate):
                sum_acceptable_votes[int(ranked_list[j])] += 1
    return sum_acceptable_votes


def main():
    if len(sys.argv) != 2:
        raise Exception("usage: python acceptable_voting.py <infile>.csv")

    print('infile: ', sys.argv[1])
    infile= sys.argv[1]

    data = process_csv(infile)
    sum_acceptable_votes = compute_votes(data)
    
    print(sum_acceptable_votes)

if __name__ == '__main__':
    main()
