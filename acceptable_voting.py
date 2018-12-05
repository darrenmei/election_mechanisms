import numpy as np
import pandas as pd
import sys

from preprocess_data import *

def compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter):
    sum_acceptable_votes = np.zeros(8)

    for i in range(len(data)):
        if data[i][0] != 0 and data[i][4] == 1:
            last_acceptable_candidate = data[i][6]
            if last_acceptable_candidate > 0:
                ranked_list = data[i][5]
                for j in range(last_acceptable_candidate):
                    party = data[i][3]
                    age = data[i][0] - 1
                    race = data[i][2]
                    if race == 2 or race == 4:
                        race = 4
                    elif race == 5:
                        race = 2
                    gender = data[i][1]
                    if gender != 0:
                        gender = 1

                    corrected_vote = gender_percentage_correcter[gender] * party_percentage_correcter[party] * racial_percentage_correcter[race] * age_percentage_correcter[age]
                    sum_acceptable_votes[int(ranked_list[j])] += corrected_vote
    return sum_acceptable_votes


def main():
    if len(sys.argv) != 2:
        raise Exception("usage: python acceptable_voting.py <infile>.csv")

    print('infile: ', sys.argv[1])
    infile= sys.argv[1]

    data = process_csv(infile)
    gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter = compute_voter_statistics(data)
    sum_acceptable_votes = compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)

    print(sum_acceptable_votes)

if __name__ == '__main__':
    main()
