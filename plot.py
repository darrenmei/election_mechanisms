import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from preprocess_data import *

to_candidate = ["Gary Johnson", "Hillary Clinton", "Jill Stein", "Donald Trump", "Marco Rubio", "Bernie Sanders", "Ted Cruz", "John Kasich"]

def plotbar(xbins, diffs, slabel, bcolor):
    #plt.hist(diffs, bins=np.arange(min(diffs), max(diffs) + binwidth, binwidth), alpha = .5, align='left', color=bcolor, label=slabel)
    plt.bar(xbins, diffs, alpha = 1.0, width=.1, color=bcolor, label=slabel)



def main():
    if len(sys.argv) != 2:
        raise Exception("usage: python acceptable_voting.py <infile>.csv")

    print('infile: ', sys.argv[1])
    infile= sys.argv[1]

    data = process_csv(infile)
    gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter = compute_voter_statistics(data)
    plotvotes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)

def plotvotes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter):
    vote_counts = np.zeros((8,8))
    
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
            #vote_counts[j][int(ranked_list[j])] += corrected_vote
            vote_counts[int(ranked_list[j])][j] += corrected_vote
    print(vote_counts)
    colors = ['#5099ff', 'red', 'orange', 'yellow', 'green', 'purple', 'pink', 'brown']
    for i in range(8):
        plotbar(np.arange(2,10) - .95 + (i/8.), vote_counts[i], to_candidate[i], colors[i])
    #plotbootstrap([ms, meds, data, data0], ["mean", 'median', 'true sample', 'filtered sample'], ['red', 'blue', 'green', '#5099ff'])
    plt.xlim(left=1, right=9)
    plt.xlabel("vote rank")
    plt.ylabel("frequency")
    plt.legend(loc='upper right')
    plt.show()

    pp.print_ranked_outcomes(sum_acceptable_votes)

if __name__ == '__main__':
    main()
