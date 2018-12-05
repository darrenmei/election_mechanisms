import numpy as np
import pandas as pd
import sys
import postprocess_data as pp

from preprocess_data import *




def compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter):
    condorcet_wins = np.zeros(8)
    condorcet_losses = np.zeros(8)
    condorcet_count = np.zeros((8,8))

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
        
        for j in range(len(ranked_list)):
            rank_j = np.where(ranked_list==j)
            for k in range(j+1, len(ranked_list)):
                rank_k = np.where(ranked_list==k)
                if rank_j < rank_k:
                    condorcet_count[j][k] += corrected_vote
                elif rank_j > rank_k:
                    condorcet_count[k][j] += corrected_vote
        

    for j in range(len(ranked_list)):
        for k in range(j+1, len(ranked_list)):
            if condorcet_count[j][k] > condorcet_count[k][j]:
                condorcet_wins[j] += 1
                condorcet_losses[k] += 1
            if condorcet_count[j][k] < condorcet_count[k][j]:
                condorcet_wins[k] += 1
                condorcet_losses[j] += 1

    print(condorcet_wins)
    print(condorcet_losses)

    net_scores = np.zeros(8)
    for i in range(8):
        net_scores[i] = condorcet_wins[i] - condorcet_losses[i]

    return net_scores


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
