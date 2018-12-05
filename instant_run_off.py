import numpy as np
import pandas as pd
import sys
import postprocess_data as pp

from preprocess_data import *

def compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter):
    sum_plurality_votes = np.zeros(8)
    votes = []
    removed = set()
    weights = []
    ranks = np.zeros(8)

    for i in range(len(data)):
        if data[i][0] != 0: #and data[i][4] != 0:
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
            weights.append(corrected_vote)
            votes.append(ranked_list)
    for k in range(8):
        first_votes = np.zeros(8)
        for r in removed:
            first_votes[r] = np.inf
        for i in range(len(votes)):
            vote = votes[i]
            weight = weights[i]
            for j in range(8):
                if int(vote[j]) not in removed:
                    first_votes[int(vote[j])] += weight
                    break
        least_first = np.argmin(first_votes)
        print(first_votes)
        removed.add(least_first)
        ranks[least_first] = k+1
    return ranks


def main():
    if len(sys.argv) != 2:
        raise Exception("usage: python acceptable_voting.py <infile>.csv")

    print('infile: ', sys.argv[1])
    infile= sys.argv[1]

    data = process_csv(infile)
    gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter = compute_voter_statistics(data)
    sum_plurality_votes = compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)

    
    #print(sum_plurality_votes)
    pp.print_ranked_outcomes(sum_plurality_votes)
    #print(sum(sum_plurality_votes))
    #print(len(data))

if __name__ == '__main__':
    main()

