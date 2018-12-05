import numpy as np
import pandas as pd
import sys
import postprocess_data as pp

import acceptable_voting as av
import coombs_rule as coombs
import instant_run_off as irf
import french_election as french
import copelands_rule as copeland
import borda_count as borda
import simple_plurality as sp

import moderation_rule as moderate

from preprocess_data import *



def main():
    if len(sys.argv) != 2:
        raise Exception("usage: python acceptable_voting.py <infile>.csv")

    print('infile: ', sys.argv[1])
    infile= sys.argv[1]

    data = process_csv(infile)
    gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter = compute_voter_statistics(data)
    
    plurality_votes = sp.compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)
    acceptable_votes = av.compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)
    coombs_votes = coombs.compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)
    run_off_votes = irf.compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)
    french_votes = french.compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)
    copelands_votes = copeland.compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)
    borda_votes = borda.compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)
    moderation_votes = moderate.compute_votes(data, gender_percentage_correcter, party_percentage_correcter, racial_percentage_correcter, age_percentage_correcter)

    
    print("#####plurality votes#####")
    pp.print_ranked_outcomes(plurality_votes)
    print('\n')
    
    print("#####acceptable votes#####")
    pp.print_ranked_outcomes(acceptable_votes)
    print('\n')

    print("#####coombs rule votes#####")
    pp.print_ranked_outcomes(coombs_votes)
    print('\n')

    print("#####instant run off votes#####")
    pp.print_ranked_outcomes(run_off_votes)
    print('\n')

    print("#####french election votes#####")
    pp.print_ranked_outcomes(french_votes)
    print('\n')

    print("#####copelands rule votes#####")
    pp.print_ranked_outcomes(copelands_votes)
    print('\n')

    print("#####borda count votes#####")
    pp.print_ranked_outcomes(borda_votes)
    print('\n')

    print("#####*moderation rule votes#####")
    pp.print_ranked_outcomes(moderation_votes)
    print('\n')


if __name__ == '__main__':
    main()

