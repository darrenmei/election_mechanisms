import numpy as np
import pandas as pd
import sys
import postprocess_data as pp

from preprocess_data import *

def borda_score(vote):
   #idxs = np.argsort(vote)
   scores = np.zeros(8)
   for i in range(len(vote)):
        scores[int(vote[i])] = 8-i
   return scores

def compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter):
    sum_borda_scores = np.zeros(8)

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
            borda_scores = borda_score(ranked_list)
            sum_borda_scores = np.add(sum_borda_scores, borda_scores*corrected_vote)
            #sum_plurality_votes[int(ranked_list[0])] += corrected_vote
    return sum_borda_scores


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
