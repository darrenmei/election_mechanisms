import numpy as np
import pandas as pd
import sys
import postprocess_data as pp

from preprocess_data import *

def compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter):
    polarizations = np.zeros(8)

    acceptable_candidate_mean = 0
    corrected_vote_sum = 0
    for i in range(len(data)):
        if data[i][0] != 0:
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

            acceptable_candidate_mean += corrected_vote * data[i][6]
            corrected_vote_sum += corrected_vote

            for j in range(8):
                curr_candidate = ranked_list[j]
                if j > data[i][6]:
                    polarizations[int(curr_candidate)] += corrected_vote * ((np.abs(j - data[i][6])**2))
    print(acceptable_candidate_mean / corrected_vote_sum)
    return polarizations


def main():
    if len(sys.argv) != 2:
        raise Exception("usage: python acceptable_voting.py <infile>.csv")

    print('infile: ', sys.argv[1])
    infile= sys.argv[1]

    data = process_csv(infile)
    gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter = compute_voter_statistics(data)
    polarizations = compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)


    #print(sum_plurality_votes)
    pp.print_ranked_outcomes(polarizations)
    #print(sum(sum_plurality_votes))
    #print(len(data))

if __name__ == '__main__':
    main()
