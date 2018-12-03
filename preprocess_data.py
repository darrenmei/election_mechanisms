import numpy as np
import pandas as pd
import sys

# Data INFO:
# Column 0: Age (0 = <20, 1 = 20-31, 2 = 32-46, 3 = 47-66, 4 = > 66)
# Column 1: Gender (0 = Male, 1 = Female, 2 = Non-binary/Third Gender, 3 = Prefer not to say)
# Column 2: Race (0 = White, 1 = Black/African American, 2 = American Indian, 3 = Asian, 4 = Native Hawaiian, 5 = Other)
# Column 3: Party Preference (0 = Democrat, 1 = Republican, 2 = Independent/Other)
# Column 4: Voted/ Did not Vote (0 = No, 1 = Yes, Did not answer = 2)
# Column 5: Ranked list (each index corresponds to candidate, number represents ranking in list)
#   Indices to Candidates: 0 - Gary Johnson, 1 - Hillary Clinton, 2 - Jill Stein, 3 - Donald Trump,
#                       4 - Marco Rubio, 5 - Bernie Sanders, 6 - Ted Cruz, 7 - John Kasich
# Column 6: Last Acceptable Candidate
# Column 7: First Choice (Assigned to numbers according to indices above)

def compute_ranked_list(df_rankings):
    ranked_list = np.zeros(len(df_rankings))
    for i in range(len(ranked_list)):
        ranked_list[int(df_rankings.iloc[i]) - 1] = int(i)
    return ranked_list


def process_csv(infile):
    df = pd.read_csv(infile)
    df = df.drop([0, 1], axis = 0)
    print(df)

    data = []
    for i in range(len(df)):
        new_row = []
        row = df.iloc[i,:]
        for j in range(8):
            if j == 0:
                if row.iloc[j] == '<20': new_row.append(0)
                if row.iloc[j] == '20-31': new_row.append(1)
                if row.iloc[j] == '32-46': new_row.append(2)
                if row.iloc[j] == '47-66': new_row.append(3)
                if row.iloc[j] == '>66': new_row.append(4)
            if j == 1:
                if row.iloc[j] == 'Male': new_row.append(0)
                if row.iloc[j] == 'Female': new_row.append(1)
                if row.iloc[j] == 'Non-binary/third gender': new_row.append(2)
                if row.iloc[j] == 'Prefer not to say': new_row.append(3)
            if j == 2:
                if row.iloc[j] == 'White': new_row.append(0)
                if row.iloc[j] == 'Black or African American': new_row.append(1)
                if row.iloc[j] == 'American Indian or Alaska Native': new_row.append(2)
                if row.iloc[j] == 'Asian': new_row.append(3)
                if row.iloc[j] == 'Native Hawaiian or Pacific Islander': new_row.append(4)
                if row.iloc[j] == 'Other': new_row.append(5)
            if j == 3:
                if row.iloc[j] == 'Democrat': new_row.append(0)
                if row.iloc[j] == 'Republican': new_row.append(1)
                if row.iloc[j] == 'Independent/ Other': new_row.append(2)
            if j == 4:
                if row.iloc[j] == 'Yes': new_row.append(1)
                elif row.iloc[j] == 'No': new_row.append(0)
                else: new_row.append(2)
            if j == 5:
                candidate_rankings = compute_ranked_list(row.iloc[j:j+8])
                new_row.append(candidate_rankings)
            if j == 6:
                new_row.append(int(row.iloc[13]))
            if j == 7:
                if row.iloc[14] == 'Gary Johnson': new_row.append(0)
                if row.iloc[14] == 'Hillary Clinton': new_row.append(1)
                if row.iloc[14] == 'Jill Stein': new_row.append(2)
                if row.iloc[14] == 'Donald Trump': new_row.append(3)
                if row.iloc[14] == 'Marco Rubio': new_row.append(4)
                if row.iloc[14] == 'Bernie Sanders': new_row.append(5)
                if row.iloc[14] == 'Ted Cruz': new_row.append(6)
                if row.iloc[14] == 'John Kasich': new_row.append(7)

        data.append(new_row)
    return data


def main():
    if len(sys.argv) != 2:
        raise Exception("usage: python preprocess_data.py <infile>.csv")

    print('infile: ', sys.argv[1])
    infile= sys.argv[1]

    data = process_csv(infile)

if __name__ == '__main__':
    main()
