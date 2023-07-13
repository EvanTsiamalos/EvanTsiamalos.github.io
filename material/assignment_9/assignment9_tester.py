import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random

tol = 1e-6
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


    def testCase1():
        
        try:
            assert('df' in globals()), "The dataframe should be called `df`."
            data = pd.read_csv("https://evantsiamalos.github.io/material/datasets/pokemon.csv")
            assert(len(df) == len(data) and list(df.columns) == list(data.columns)
                  ), "You did not load the correct dataframe"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase2():
        
        try:
            assert('number_of_water' in globals()), "You should have a variable called `number_of_water`."
            assert(number_of_water == len(df[df["Type1"] == "water"])
                  ), "The calculation of `number_of_water` is not correct."
            assert('prob_water' in globals()), "You should have a variable called `prob_water`."
            assert( prob_water == number_of_water/len(df) or math.isclose(prob_water,number_of_water/len(df),tol)
                  ), "The calculation of `prob_water` is not correct."
            
            
            
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase3():
        
        try:
            
            assert('catch10' in [f.__name__ for f in globals().values() if type(f) == type(lambda *args: None)]), "You should have a function called `catch10`."
            result = catch10()
            assert(type(result) == int and result >=0 and result <= 10
                  ), "The function `catch10` should return an integer between 0 and 10."
            results = np.array([catch10() for i in range(1000)])
            assert(((results >= 0 ) & (results <= 10)).all() and np.unique(results).size>=4
                  ),"The function `catch10` does not work properly" 
            
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase4():
        
        try:
            
            assert("df_water" in globals()
                  ), "The simulation dataframe should be called `df_water`"
            assert(isinstance(df_water,pd.core.frame.DataFrame)
                  ), "`df_water` should be a dataframe"
            assert(len(list(df_water.columns)) == 1 and "number_of_water" in 
                  df_water.columns), '''The `df_water` dataframe should have
            one column called `number_of_water`'''
            
            
            assert(len(df_water) == 1000
            ),'''The simulation dataframe `df_water` should have 1000 rows'''
            vals = df_water["number_of_water"].values
            assert(
            df_water["number_of_water"].dtype == "int64" and ((vals >= 0) & (vals<=10)).all()
            ), '''`df_water` should contain integers from 0 to 10'''
            assert(np.unique(vals).size >= 5
                  ), '''`df_water` should take more than 5 values'''
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase5():
        
        try:
            assert('no_secondary' in globals()
                  ), "You should have a variable called `no_secondary`."
            assert(no_secondary == len(df[df["Type2"] == "None"])
                  ), "The calculation of `no_secondary` is not correct."
            assert('prob_secondary' in globals()
                  ), "You should have a variable called `prob_secondary`."
            assert(1 - no_secondary/len(df)==prob_secondary or  math.isclose(prob_secondary,1 - no_secondary/len(df),abs_tol=tol )
                  ), "The calculation of `prob_secondary` is not correct."
            
            
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase6():
        
        try:
            assert("secondary_ev" in globals()
                  ),'''You should have a variable called `secondary_ev`'''
            
            assert(secondary_ev == 5*prob_secondary
                  ),'''The calculation of `secondary_ev` is not correct.'''
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
            
    def testCase7():
        
        try:
            
            assert('catch5' in [f.__name__ for f in globals().values() if type(f) == type(lambda *args: None)]), "You should have a function called `catch5`."
            result = catch5()
            assert(type(result) == int and result >=0 and result <= 5
                  ), "The function `catch5` should return an integer between 0 and 5."
            results = np.array([catch5() for i in range(10000)])
            assert(((results >= 0 ) & (results <= 5)).all() and np.unique(results).size>=4
                  ),"The function `catch5` does not work properly" 
            
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase8():
        
        try:
            
            assert("df_secondary" in globals()
                  ), "The simulation dataframe should be called `df_secondary`"
            assert(isinstance(df_secondary,pd.core.frame.DataFrame)
                  ), "`df_secondary` should be a dataframe"
            assert(len(list(df_secondary.columns)) == 1 and "secondary" in 
                  df_secondary.columns), '''The `df_secondary` dataframe should have
            one column called `secondary`'''
            
            
            assert(len(df_secondary) == 1000
            ),'''The simulation dataframe `df_secondary` should have 1000 rows'''
            vals = df_secondary["secondary"].values
            assert(
            df_secondary["secondary"].dtype == "int64" and ((vals >= 0) & (vals<=5)).all()
            ), '''`df_secondary` should contain integers from 0 to 10'''
            assert(np.unique(vals).size >= 5
                  ), '''`df_secondary` should take more than 5 values'''
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase9():
        
        try:
            assert('catch_average' in [f.__name__ for f in globals().values() if type(f) == type(lambda *args: None)]
                  ), "You should have a function called `catch_average`."
            
            result = catch_average("HP", 8)
            assert(isinstance(result, float)
                  ), '''`catch_average` should return a number'''
            
            assert(math.isclose(catch_average("HP", 10000), df["HP"].mean(),rel_tol= 0.01)
                  ),'''`catch_average` does not work properly.'''

            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)