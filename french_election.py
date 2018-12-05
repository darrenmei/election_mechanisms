import numpy as np
import pandas as pd
import sys

from preprocess_data import *

def compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter):
    sum_plurality_votes = np.zeros(8)

    # first round
    for i in range(len(data)):
        if data[i][0] != 0 and data[i][4] != 0:
            first_round_vote = data[i][7]
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
            sum_plurality_votes[int(first_round_vote)] += corrected_vote

    top_two_candidates = [0, 0]
    for i in range(8):
        if sum_plurality_votes[i] > (len(data) / 2):
            return sum_plurality_votes
        if sum_plurality_votes[i] > min(sum_plurality_votes[top_two_candidates[0]], sum_plurality_votes[top_two_candidates[1]]):
            if sum_plurality_votes[top_two_candidates[0]] == min(sum_plurality_votes[top_two_candidates[0]], sum_plurality_votes[top_two_candidates[1]]):
                top_two_candidates[0] = i
            else:
                top_two_candidates[1] = i

    #runoff
    print(top_two_candidates)
    runoff_votes = np.zeros(2)
    for i in range(len(data)):
        if data[i][0] != 0 and data[i][4] != 0:
            ranked_list = data[i][5]

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

            found_first = False
            j = 0
            while found_first is False:
                if ranked_list[j] == top_two_candidates[0]:
                    runoff_votes[0] += corrected_vote
                    found_first = True
                elif ranked_list[j] == top_two_candidates[1]:
                    runoff_votes[1] += corrected_vote
                    found_first = True
                j += 1
    return runoff_votes


def main():
    if len(sys.argv) != 2:
        raise Exception("usage: python acceptable_voting.py <infile>.csv")

    print('infile: ', sys.argv[1])
    infile= sys.argv[1]

    data = process_csv(infile)
    gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter = compute_voter_statistics(data)
    sum_plurality_votes = compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)

    print(sum_plurality_votes)


if __name__ == '__main__':
    main()
