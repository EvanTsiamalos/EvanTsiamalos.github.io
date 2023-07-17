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
            assert("df_1" in globals()
                  ), "You should have a dataframe called `df_1`"
            
            
            assert(len(df_1) == len(pd.read_csv("https://evantsiamalos.github.io/material/datasets/sleep.csv"))
                  ), "The dataframe that you loaded is not correct"
            m1_ = df_1["Hours of sleep"].mean()

            v1_ = df_1["Hours of sleep"].var()

            n1_ = len(df_1)

            a1_ = 1 - 0.95

            za1_ = st.norm(0,1).ppf(1-a1_/2)
            ans_a_1 = m1_ - za1_ * math.sqrt(v1_/n1_)
            ans_b_1 = m1_ + za1_ * math.sqrt(v1_/n1_)
            
            assert("a_1" in globals()
                  ), "You should have a variable called `a_1`"
            assert("b_1" in globals()
                  ), "You should have a variable called `b_1`"
            assert(
                (ans_a_1 == a_1) or (math.isclose(ans_a_1,a_1)) and 
                ( (ans_b_1 == b_1) or (math.isclose(ans_b_1,b_1)))
            ), "The calculation of the confidence interval is not correct"

            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            

    def testCase2():
        try:
            assert("df_2" in globals()
                  ), "You should have a dataframe called `df_2`"
            
            
            assert(len(df_2) == len(pd.read_csv("https://evantsiamalos.github.io/material/datasets/ds_salaries.csv"))
                  ), "The dataframe that you loaded is not correct"
            
            
            assert("df_2_clean" in globals()
                  ), "You should have a dataframe called `df_2_clean`"
            
            col_ = df_2["salary_in_usd"]
            q1_ = col_.quantile(0.25)
            q3_ = col_.quantile(0.75)
            IQR_ = q3_-q1_
            
            clean_dataset_ = df_2[
    (df_2["salary_in_usd"] >= q1_ - 1.5*IQR_) & (df_2["salary_in_usd"] <= q3_ + 1.5*IQR_)
]

            assert(len(df_2_clean) == len(clean_dataset_)
                  ), "The `df_2_clean` dataframe is not correct"
            

            
            
            m2_ = df_2_clean["salary_in_usd"].mean()

            v2_ = df_2_clean["salary_in_usd"].var()

            n2_ = len(df_2_clean)

            a2_= 1 - 0.99

            za2_ = st.norm(0,1).ppf(1-a2_/2)
            
            ans_a_2 = m2_ - za2_ * math.sqrt(v2_/n2_)
            ans_b_2 = m2_ + za2_ * math.sqrt(v2_/n2_)
            assert("a_2" in globals()
                  ), "You should have a variable called `a_2`"
            assert("b_2" in globals()
                  ), "You should have a variable called `b_2`"
            assert(
                (ans_a_2 == a_2) or (math.isclose(ans_a_2,a_2)) and 
                ( (ans_b_2 == b_2) or (math.isclose(ans_b_2,b_2)))
            ), "The calculation of the confidence interval is not correct"

            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

            
    def testCase3():
        try:
            assert("df_3" in globals()
                  ), "You should have a dataframe called `df_3`"
            
            
            assert(len(df_3) == 100
                  ), "The dataframe `df_3` that  is not correct"
            m3_ = df_3["answers"].mean()

            v3_ = df_3["answers"].var()

            n3_ = len(df_3)

            a3_ = 1 - 0.9

            za3_ = st.norm(0,1).ppf(1-a3_/2)
            ans_a_3 = m3_ - za3_ * math.sqrt(v3_/n3_)
            ans_b_3 = m3_ + za3_ * math.sqrt(v3_/n3_)
            
            assert("a_3" in globals()
                  ), "You should have a variable called `a_3`"
            assert("b_3" in globals()
                  ), "You should have a variable called `b_3`"
            assert(
                (ans_a_3 == a_3) or (math.isclose(ans_a_3,a_3)) and ((ans_b_3 == b_3) or (math.isclose(ans_b_3,b_3)))
            ), "The calculation of the confidence interval is not correct"

            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
