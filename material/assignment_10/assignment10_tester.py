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
            assert("probability_1" in globals()
                  ), "You should have a variable called `probability_1`"
            ans =st.norm(15.5, math.sqrt(6/35)).cdf(12.5)
            assert(probability_1 == ans or math.isclose(probability_1, ans, rel_tol=tol)
                  ), "The calculation of `probability_1` is not correct"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            

            
    def testCase2():
        try:
            assert("df_2" in globals()
                  ), "You should have a dataframe called `df_2`"
            
            assert(len(df_2) ==len(pd.read_csv("https://evantsiamalos.github.io/material/datasets/sleep.csv"))
                  ), "The dataframe that you loaded is not correct"
            
            assert("sample_size_2" in globals()
                  ), "You should have a variable called `sample_size_2`"
           
            assert(sample_size_2 == len(df_2)
                  ), "`sample_size_2` is not correct"
            
            assert("sample_average_2" in globals()
                  ), "You should have a variable called `sample_average_2`"
           
            assert(sample_average_2 == df_2["Hours of sleep"].mean()
                  ), "`sample_average_2` is not correct"
            
            assert("sample_variance_2" in globals()
                  ), "You should have a variable called `sample_variance_2`"
           
            assert(sample_variance_2 == df_2["Hours of sleep"].var()
                  ), "`sample_size_2` is not correct"
            ans = 1 - st.norm(mu, math.sqrt(sample_variance_2/sample_size_2)).cdf(sample_average_2)
            assert(probability_2 == ans or math.isclose(probability_2, ans, rel_tol=tol)
                  ), "The calculation of `probability_2` is not correct"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)


            
    def testCase3():
        try:
            assert("probability_3" in globals()
                  ), "You should have a variable called `probability_3`"
            m_ = 0.65
            v_= 0.65 * (1 - 0.65)

            s_ = 100

            ans = st.norm(m_, math.sqrt(v_/s_)).cdf(56/s_)
            assert(probability_3 == ans or math.isclose(probability_3, ans, rel_tol=tol)
                  ), "The calculation of `probability_3` is not correct"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            