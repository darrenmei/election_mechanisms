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

to_candidate = ["Gary Johnson", "Hillary Clinton", "Jill Stein", "Donald Trump", "Marco Rubio", "Bernie Sanders", "Ted Cruz", "John Kasich"]

def print_ranked_outcomes(arr):
    sorted_arr = []
    while len(sorted_arr) < 8:
        max_idx = 0
        for i in range(len(arr)):
            if arr[i] > arr[max_idx]:
                max_idx = i
        sorted_arr.append(to_candidate[max_idx] + ": " + str(arr[max_idx]))
        arr[max_idx] = -999
    
    for msg in sorted_arr:
        print(msg) 
