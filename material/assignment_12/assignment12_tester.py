import math 
import scipy.stats as st
tol = 1e-9
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
            assert("df" in globals()
                  ), "You should have a dataframe called `df`"
            
            assert(len(df) == len(pd.read_csv("https://evantsiamalos.github.io/material/datasets/hello.csv")
                                 )), "The dataframe `df` is not the right one"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            

    def testCase2():
        try:
            assert("sleep_column_name" in globals()
                  ), "You should have a variable called `sleep_column_name`"
            
            assert(isinstance(sleep_column_name, str) and sleep_column_name == "How many hours do you sleep in a day?"
                  ), "The variable `sleep_column_name` is not correct. It should only be the name of the column"
            
            
            assert("sleep_average" in globals()
                  ), "You should have a variable called `sleep_average`"
            assert(sleep_average == df[sleep_column_name].mean()
                  ), ''' `sleep_average` is not correct
                  '''
            
            
            
            
            assert("sleep_var" in globals()
                  ), "You should have a variable called `sleep_var`"
            
            assert(sleep_var == df[sleep_column_name].var()
                  ), ''' `sleep_var` is not correct
                  '''
            
            assert("sample_size" in globals()
                  ), "You should have a variable called `sample_size`"
            assert(sample_size == len(df)
                  ), '`sample_size` is not correct'

            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase3():
        try:
            assert("test_statistic" in globals()
                  ), "You should have a variable called `test_statistic`"
            assert(test_statistic == (sleep_average - 6.8)/math.sqrt(sleep_var/sample_size)
or math.isclose(test_statistic,  (sleep_average - 6.8)/math.sqrt(sleep_var/sample_size) 
               )                  ), ''' `test_statistic` is not correct'''
            
            
            
            assert("p_value" in globals()
                  ), "You should have a variable called `p_value`"
            
            
            assert(p_value == 2* ( 1 - st.norm(0,1).cdf(test_statistic))
                  or math.isclose(p_value, 2* ( 1 - st.norm(0,1).cdf(test_statistic)))
                  ),  ''' `p_value` is not correct'''
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase4():
        try:
            assert("sleep_results" in globals()
                  ), "You should have a variable called `sleep_results`"
            assert(isinstance(sleep_results, tuple) and math.isclose(sleep_results[1], 
                                                                    p_value)
                  ), ''' `sleep_results` is not correct'''
            
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
            
    def testCase5():
        try:
            assert("party_question" in globals()
                  ), "You should have a variable called `party_question`"
            
            assert(isinstance(party_question, str) 
                   and party_question == "In the past year, how many times have you been to the party?"
                  ), "The variable `party_question` is not correct. It should only be the name of the column"

            assert("party_column_clean" in globals()
                  ),"You should have a variable called `party_column_clean`"
            col_=df[party_question].dropna() 
            assert(isinstance(party_column_clean,type(col_))
                  and len(party_column_clean) == len(col_) 
                  
                  ),''' `party_column_clean` is not correct'''
            
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase6():
        try:
            assert("party_results" in globals()
                  ), "You should have a variable called `party_results`"
            
            ans_ = weightstats.ztest(party_column_clean, value = 5, alternative="larger")

            assert(isinstance(party_results, tuple) and party_results[1] ==
                                                                    ans_[1]
                  ), ''' `party_results` is not correct'''
            
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
             
    def testCase7():
        try:
            assert("credits_question" in globals()
                  ), "You should have a variable called `credits_question`"
            
            assert(isinstance(credits_question, str) 
                   and credits_question == "How many credit hours are you taking?"
                  ), "The variable `credits_question` is not correct. It should only be the name of the column"

            
            assert("happiness_question" in globals()
                  ), "You should have a variable called `happiness_question`"
            
            assert(isinstance(happiness_question, str) 
                   and happiness_question == "From 1 to 10, how happy are you right now?"
                  ), "The variable `happiness_question` is not correct. It should only be the name of the column"


            df_1_ans = df[[credits_question, happiness_question]]
            assert("df_1" in globals()
                  ), "You should have a variable called `df_1`"
            
            assert(isinstance(df_1, type(df_1_ans))
                  and len(df_1) == len(df_1_ans) and 
                   len(df_1) == len(df_1_ans) and 
                   happiness_question in df_1.columns and 
                   credits_question in df_1.columns
                   
                  ), "`df_1` is not correct"
            
            df_clean_ans = df_1[
    (df_1[credits_question] <= 25) & (df_1[happiness_question] <= 10)
].dropna()
            assert("df_clean" in globals()
                  ), "You should have a variable called `df_clean`"
            
            assert(isinstance(df_clean, type(df_clean_ans))
                  and len(df_clean) == len(df_clean_ans) 

                   
                  ), "`df_clean` is not correct"
            
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

            
    def testCase8():
        try:
            df_many_credits_ans = df_clean[df_clean[credits_question] >= 15]
            assert("df_many_credits" in globals()
                  ), "You should have a variable called `df_many_credits`"
            
            assert(isinstance(df_many_credits, type(df_many_credits_ans))
                  and len(df_many_credits) == len(df_many_credits_ans)  

                   
                  ), "`df_many_credits` is not correct"
            
            df_less_credits_ans = df_clean[df_clean[credits_question] < 15]
            assert("df_less_credits" in globals()
                  ), "You should have a variable called `df_less_credits`"
            
            assert(isinstance(df_less_credits, type(df_less_credits_ans))
                  and len(df_less_credits) == len(df_less_credits_ans)

                   
                  ), "`df_less_credits` is not correct"
            

            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

            

    def testCase9():
        try:
            assert("happy_results" in globals()
                  ), "You should have a variable called `happy_results`"
            
            ans_ = weightstats.ztest(df_many_credits[happiness_question], df_less_credits[happiness_question], alternative='smaller')
            

            assert(isinstance(happy_results, tuple) and happy_results[1] ==
                                                                    ans_[1]
                  ), ''' `happy_results` is not correct'''
            
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
             