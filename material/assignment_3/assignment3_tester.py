
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
            assert('df' in globals()), "You do not have a DataFrame called `df`."
            assert( len(df) == len(pd.read_csv("https://evantsiamalos.github.io/material/datasets/salary.csv") )), "This is not the right dataframe"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
                   
    def testCase2():
        try:
            salary_col = df["Present Salary"]
            for vvar in ["num_employee", "mean_sal", "median_sal", "std_sal", "min_sal", "max_sal"]:
                   assert( vvar in globals()),f"You have not defined a variable called `{vvar}`"
            assert(num_employee == len(df)), "`num_emploee` was not calculated correctly"
            assert(mean_sal == salary_col.mean()), "`mean_sal` was not calculated correctly"      
            assert(median_sal == salary_col.median()), "`median_sal` was not calculated correctly"
            assert(std_sal == salary_col.std()), "`std_sal` was not calculated correctly"       
            assert(min_sal == salary_col.min()), "`min_sal` was not calculated correctly"
            assert(max_sal == salary_col.max()), "`max_sal` was not calculated correctly"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
            
    def testCase3():
        try:
            for vvar in ["top_10", "lowest_5", "quantile_99", "top_1_percent"]:
                assert( vvar in globals()),f"You have not defined a variable called `{vvar}`"
#             assert(top_10["Present Salary"].eq(df.nlargest(10, "Present Salary")["Present Salary"])).all(),"`top_10` was not calculated correctly"
#             assert(lowest_5["Present Salary"].eq(df.nsmallest(5, "Present Salary")["Present Salary"])).all(),"`lowest_5` was not calculated correctly"
            assert(quantile_99 == df["Present Salary"].quantile(0.99)),"`quantile_99` was not calculated correctly"
#             assert(top_1_percent["Present Salary"].eq(df[df["Present Salary"] >= quantile_99]["Present Salary"])).all(),"`top_1_percent` was not calculated correctly"
            ans1 = df.nlargest(10, "Present Salary")
            ans2 = df.nsmallest(5,"Present Salary")
            ans3 = df[df["Present Salary"] >= quantile_99]
            assert((len(top_10) == len(ans1) ) & (ans1["Present Salary"].min() == top_10["Present Salary"].min())),"`top_10` was not calculated correctly"
            assert((len(lowest_5) == len(ans2) ) & (ans2["Present Salary"].max() == lowest_5["Present Salary"].max())),"`lowest_5` was not calculated correctly"
            assert((len(top_1_percent) == len(ans3) ) & (ans3["Present Salary"].min() == top_1_percent["Present Salary"].min())),"`top_1_percent` was not calculated correctly"
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)        
    def testCase4():
        try:
            for vvar in ["df2", "agg_mean_df"]:
                assert( vvar in globals()),f"You have not defined a variable called `{vvar}`"
            cols = df2.columns.to_list()
            assert len(df2) == len(df), "df2 not calculated correctly"
            assert(  
                len(cols) == 2 and "Department Name" in cols and "Present Salary" in cols
            ),"We should only keep the columns `Department Name` and `Present Salary` in df2"
            ans1 = df2.groupby("Department Name").agg("mean").reset_index()
            assert(
                len(agg_mean_df) == len(ans1)
            ), "`agg_mean_df` was not calculated correctly"
            assert(
                agg_mean_df["Present Salary"].sum() == ans1["Present Salary"].sum()
            ), "`agg_mean_df` was not calculated correctly"
            
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
    def testCase5():
        try:
            for vvar in ["mean_eng", "mean_psych", "mean_ece"]:
                assert( vvar in globals()),f"You have not defined a variable called `{vvar}`"
            assert(
                mean_eng.iloc[0] == agg_mean_df[agg_mean_df["Department Name"]=="English"]["Present Salary"].iloc[0]
                ), "`mean_eng` was not calculated correctly" 
            assert(
                mean_psych.iloc[0] == agg_mean_df[agg_mean_df["Department Name"]=="Psychology"]["Present Salary"].iloc[0]
                ), "`mean_psych` was not calculated correctly"
            assert(
                mean_ece.iloc[0] == agg_mean_df[agg_mean_df["Department Name"]=="Electrical & Computer Eng"]["Present Salary"].iloc[0]
                ), "`mean_ece` was not calculated correctly"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
                   
    def testCase6():
        try:
            for vvar in ["top_10_paying_departments", "lowest_10_paying_departments"]:
                assert( vvar in globals()),f"You have not defined a variable called `{vvar}`"
            ans1 = agg_mean_df.nlargest(10, "Present Salary")
            ans2 = agg_mean_df.nsmallest(10,"Present Salary")
            assert(
                len(top_10_paying_departments) == 10
            ),"`top_10_paying_departments` was not calculated correctly"
            assert(
                len(lowest_10_paying_departments) == 10
            ),"`lowest_10_paying_departments` was not calculated correctly"
            assert (
                ans1["Present Salary"].sum() == top_10_paying_departments["Present Salary"].sum()
            ), "`top_10_paying_departments` was not calculated correctly"
            assert (
                ans2["Present Salary"].sum() == lowest_10_paying_departments["Present Salary"].sum()
            ), "`lowest_10_paying_departments` was not calculated correctly"            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
                   
    def testCase7():
        try:
            for vvar in ["agg_count_df"]:
                assert( vvar in globals()),f"You have not defined a variable called `{vvar}`"
            cols = agg_count_df.columns.to_list()
            assert(  
                len(cols) == 2 and "Department Name" in cols and "Num Employees" in cols
            ),"We should have the columns `Department Name` and `Num Employees` in agg_count_df"
            ans1 = df2.groupby("Department Name").agg("count").reset_index()
            ans1.rename(columns={"Present Salary": "Num Employees"}, inplace=True)
            assert(
                len(agg_count_df) == len(ans1)
            ), "`agg_count_df` was not calculated correctly"
            assert(
                agg_count_df["Num Employees"].sum() == ans1["Num Employees"].sum()
            ), "`agg_count_df` was not calculated correctly"
            
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
                   
    def testCase8():
        try:
            for vvar in ["eng_employees", "psych_employees", "ece_employees"]:
                assert( vvar in globals()),f"You have not defined a variable called `{vvar}`"
            assert(
                eng_employees.iloc[0] == agg_count_df[agg_mean_df["Department Name"]=="English"]["Num Employees"].iloc[0]
                ), "`eng_employees` was not calculated correctly" 
            assert(
                psych_employees.iloc[0] == agg_count_df[agg_mean_df["Department Name"]=="Psychology"]["Num Employees"].iloc[0]
                ), "`psych_employees` was not calculated correctly"
            assert(
                ece_employees.iloc[0] == agg_count_df[agg_mean_df["Department Name"]=="Electrical & Computer Eng"]["Num Employees"].iloc[0]
                ), "`ece_employees` was not calculated correctly"
            print(f"\N{PARTY POPPER} All tests passed! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)                   