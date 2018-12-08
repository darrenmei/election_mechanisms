import numpy as np
import pandas as pd
import sys
import postprocess_data as pp

from preprocess_data import *

to_candidate = ["Gary Johnson", "Hillary Clinton", "Jill Stein", "Donald Trump", "Marco Rubio", "Bernie Sanders", "Ted Cruz", "John Kasich"]

def compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter):
    switches = np.zeros((8,8))

    for i in range(len(data)):
        if data[i][0] != 0: #and data[i][4] != 0:
            ranked_list = data[i][5]
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

            top_vote = ranked_list[0]
            if top_vote != first_round_vote:
                switches[int(top_vote)][int(first_round_vote)] += corrected_vote
                if top_vote == 3. and first_round_vote == 5.:
                    print(ranked_list)
                    print(data[i][6])
    for i in range(8):
        for j in range(8):
            if switches[i][j] > 5:
                print(str(switches[i][j]) + " switch from " + to_candidate[i] + " to " + to_candidate[j])

    print(sum(sum(switches)))
    return switches 


def main():
    if len(sys.argv) != 2:
        raise Exception("usage: python acceptable_voting.py <infile>.csv")

    print('infile: ', sys.argv[1])
    infile= sys.argv[1]

    data = process_csv(infile)
    gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter = compute_voter_statistics(data)
    sum_plurality_votes = compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)

    
    #print(sum_plurality_votes)
    #pp.print_ranked_outcomes(sum_plurality_votes)
    #print(sum(sum_plurality_votes))
    #print(len(data))

if __name__ == '__main__':
    main()
