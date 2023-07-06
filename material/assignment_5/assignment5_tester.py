
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
            assert('df_1' in globals()), "You do not have a DataFrame called `df_1`."
            assert( len(df_1) == 100), "The dataframe was not created correctly"
            assert( "coin_1" in list(df_1.columns)), "The dataframe df_1 should have a column called `coin_1`"
            assert( "coin_2" in list(df_1.columns)), "The dataframe df_1 should have a column called `coin_2`"
            assert( "coin_3" in list(df_1.columns)), "The dataframe df_1 should have a column called `coin_3`"
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase2():
        try:       
            assert 'successful_cases_1' in globals() , "You do not have a variable called `successful_cases_1`." 
            assert type(successful_cases_1) == int, "The variable `successful_cases_1` should be a number"
            assert successful_cases_1 == len(df_1[(df_1["coin_1"] == "H") & (df_1["coin_2"] == "T") & (df_1["coin_3"] == "H")]
                                            ), "The calculation of `successful_cases_1` is not correct"
            
            assert 'probability_1' in globals() , "You do not have a variable called `probability_1`."
            assert probability_1 == successful_cases_1/100 , "The calculation of `successful_cases_1` is not correct"
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
                   
    def testCase3():
        try:
            assert('df_2' in globals()), "You do not have a DataFrame called `df_2`."
            assert( len(df_2) == 1000), "The dataframe was not created correctly"
            assert( "wheel_1" in list(df_2.columns)), "The dataframe df_2 should have a column called `wheel_1`"
            assert( "wheel_2" in list(df_2.columns)), "The dataframe df_2 should have a column called `wheel_2`"
            assert( "wheel_3" in list(df_2.columns)), "The dataframe df_2 should have a column called `wheel_3`"
            assert( "wheel_4" in list(df_2.columns)), "The dataframe df_2 should have a column called `wheel_4`"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase4():
        try:       
            assert 'successful_cases_2' in globals() , "You do not have a variable called `successful_cases_2`." 
            assert type(successful_cases_2) == int, "The variable `successful_cases_2` should be a number"
            assert successful_cases_2 == len(df_2[
    (df_2["wheel_1"] < df_2["wheel_2"])  |  (df_2["wheel_3"] > df_2["wheel_4"])
]), "The calculation of `successful_cases_1` is not correct"
            
            assert 'probability_2' in globals() , "You do not have a variable called `probability_2`."
            assert probability_2 == successful_cases_2/1000 , "The calculation of `successful_cases_2` is not correct"
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
            
    def testCase5():
        try:
            assert('poll' in globals()), "You should have a variable called `poll`."
            assert( len(poll) == 100), "The variable `poll` should be a list with 100 elements"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
            
    def testCase6():
        try:
            assert('positive_answers' in globals()), "You should have a variable called `positive_answers`."

            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
            
            
    def testCase7():
        try:
            assert('df_3' in globals()), "You do not have a DataFrame called `df_3`."
            assert( len(df_3) == 10000), "The dataframe was not created correctly"
            assert( "positive_answers" in list(df_3.columns)), "The dataframe df_3 should have a column called `positive_answers`"
            
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