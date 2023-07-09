import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class Tester:
    def stock_example():


        import matplotlib.pyplot as plt
        import random
        import pandas as pd
        xx = []
        c = 100
        for i in range(50):
            xx.append(c)
            c += random.choice([-1,1])


        plt.plot(xx,  "o-")
        plt.xlabel("Day")
        plt.ylabel("Price")
        plt.grid()

    def testCase1():
        
        try:
            assert('simulate_game' in globals()), "You should have a function called `simulate_game`."
            
            results = np.array([simulate_game() for i in range(10000) ])
            
            flag = True
            s = 0
            for i in range(9):
                if i <= 5:
                    assert i in results, "The function `simulate_game` does not work properly"
                s += results[results == i].size
            assert s == results.size, "The function `simulate_game` does not work properly"
            assert 1.9<= results.mean() and results.mean()<= 2.1, "The function `simulate_game` does not work properly"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase2():
        try:       
            assert 'df_1' in globals() , "You don't have a variable called `df_1`." 
            assert len(df_1) == 1000, f"You should simulate the game for 1000 times; you simulated for {len(df_1)} times"
            assert len(df_1.columns) == 1 and "outcome" in df_1.columns, "The dataframe `df_1` should only have one column called `outcome`"
            assert df_1["outcome"].dtype =='int64', "The dataframe should contain integers from 0 to 8."
            assert (set(df_1["outcome"].unique()).issubset(set(range(9)))
                   ), "The values in `df_1` should only be between 0 and 8"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
                   
    def testCase3():
        try:
            assert('mean_outcome' in globals()), "You do not have a variable called `mean_outcome`."
            assert(mean_outcome == df_1["outcome"].mean() or math.isclose(mean_outcome, df_1["outcome"].mean(), rel_tol= 1e-6)
                  ), "The calculation of `mean_outcome` is not correct"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase4():
        try:       
            assert 'probability_1' in globals() , "You do not have a variable called `probability_1`." 
            assert(type(probability_1) == float and probability_1 <= 1 and probability_1 >= 0
                  ), "`probability_1` should be a number between 0 and 1"
            assert( probability_1 == len(df_1[df_1["outcome"] >= 5]) / len(df_1)
                  ), "The calculation of `probability_1` is not correct"
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
            
    def testCase5():
        try:
            assert('simulate_stock' in globals()), "You should have a function called `simulate_stock`."
            
            results = np.array([simulate_stock(50) for i in range(10000) ])
            assert(((results > 100) | (results > 100) ).sum() > 0
                  ), "The `simulate_stock` function does not work properly"
            assert( results.mean() >=98 and results.mean() <= 102
                  ), "The `simulate_stock` function does not work properly"

            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
            
    def testCase6():
        try:
            assert 'df_2' in globals() , "You don't have a variable called `df_2`." 
            assert len(df_2) == 10000, f"You should simulate  for 10000 times; you simulated for {len(df_2)} repetitions"
            assert len(df_2.columns) == 1 and "price" in df_2.columns, "The dataframe `df_2` should only have one column called `price`"
            assert df_2["price"].dtype =='int64', "The dataframe should contain integers."            
            
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
            
            
    def testCase7():
        try:
            assert 'probability_2' in globals() , "You do not have a variable called `probability_2`." 
            assert(type(probability_2) == float and probability_2 <= 1 and probability_2 >= 0
                  ), "`probability_2` should be a number between 0 and 1"
            assert( probability_2 == len(df_2[df_2["price"] >= 105]) / len(df_2)
                  ), "The calculation of `probability_2` is not correct"
            
    
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase8():
        try:       
            assert 'successful_cases_3' in globals() , "You do not have a variable called `successful_cases_3`." 
            assert type(successful_cases_3) == int, "The variable `successful_cases_3` should be a number"
            assert successful_cases_3 == len(df_3[(df_3["positive_answers"] <= 56) ]
                                            ), "The calculation of `successful_cases_3` is not correct"
            
            assert 'probability_3' in globals() , "You do not have a variable called `probability_3`."
            assert probability_3 == successful_cases_3/10000 , "The calculation of `successful_cases_3` is not correct"
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)