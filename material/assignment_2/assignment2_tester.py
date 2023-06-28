





class Tester:
     
    ## import urllib
    ## _j = "https://evantsiamalos.github.io/material/assignment_2/assignment2_tester.py"
    ## _ = urllib.request.urlopen(_j).read()
    ## exec(_)
    ## Tester.testCase1()
    

    def testCase1():
        try:
            assert('df' in globals()), "You do not have a DataFrame called `df`."
            assert(len(df) == 64048 ), "This is not the right dataframe"
            print("Test Passed: \u2714")
        except AssertionError as msg:
            print("-"*10 + " ERROR " + "-"*10)
            print(msg)
    def testCase2():
        try:
            assert('df_STAT' in globals()), "You do not have a DataFrame called `df_STAT`."
            assert('df_CS' in globals()), "You do not have a DataFrame called `df_CS`."
            assert( (df_STAT["Subject"] == "STAT").all()), "df_STAT has non-STAT courses in it"
            assert( (df_CS["Subject"] == "CS").all()), "df_CS has non-CS courses in it"
            assert(len(df_STAT) == len(df[df["Subject"] == "STAT"])), "df_STAT was not created correctly"
            assert(len(df_CS) == len(df[df["Subject"] == "CS"])), "df_CS was not created correctly"
            print("Test Passed: \u2714")
        except AssertionError as msg:
            print("-"*10 + " ERROR " + "-"*10)
            print(msg)
            
    def testCase3():
        try:
            assert('average_percentage_STAT' in globals()), "You do not have a DataFrame called `average_percentage_STAT`."
            assert('average_percentage_CS' in globals()), "You do not have a DataFrame called `average_percentage_CS`."
            assert(average_percentage_STAT == df_STAT["Percentage of As"].mean()), "`average_percentage_STAT` was not calculated correctly"
            assert(average_percentage_CS == df_CS["Percentage of As"].mean()), "`average_percentage_CS` was not calculated correctly"
            print("Test Passed: \u2714")
        except AssertionError as msg:
            print("-"*10 + " ERROR " + "-"*10)
            print(msg)        
    def testCase4():
        try:
            assert('df_cs_recent' in globals()), "You do not have a DataFrame called `df_cs_recent`."
            assert('df_cs_old' in globals()), "You do not have a DataFrame called `df_cs_old`."
            assert('df_stat_recent' in globals()), "You do not have a DataFrame called `df_stat_recent`."
            assert('df_stat_old' in globals()), "You do not have a DataFrame called `df_stat_old`."
            ans1 = df_CS[df_CS["Year"] >= 2021]
            ans2 = df_CS[df_CS["Year"] < 2021]
            ans3 = df_STAT[df_STAT["Year"] >= 2021]
            ans4 = df_STAT[df_STAT["Year"] < 2021]
            assert((df_cs_recent["Year"] >= 2021).all() and df_cs_recent["Subject"]=="CS").all(), "`df_cs_recent` dataframe is not correct"
            assert((df_cs_old["Year"] < 2021).all() and df_cs_old["Subject"]=="CS").all(), "`df_cs_old` dataframe is not correct"
            assert((df_stat_recent["Year"] >= 2021).all() and df_stat_recent["Subject"]=="STAT").all(), "`df_stat_recent` dataframe is not correct"
            assert((df_stat_old["Year"] < 2021).all() and df_stat_old["Subject"]=="STAT").all(), "`df_stat_old` dataframe is not correct"
            assert(len(df_cs_recent) == len(ans1)), "`df_cs_recent` dataframe is not correct"
            assert(len(df_cs_old) == len(ans2)), "`df_cs_old` dataframe is not correct"
            assert(len(df_stat_recent) == len(ans3)), "`df_stat_recent` dataframe is not correct"
            assert(len(df_stat_old) == len(ans4)), "`df_stat_old` dataframe is not correct"
            print("Test Passed: \u2714")
        except AssertionError as msg:
            print("-"*10 + " ERROR " + "-"*10)
            print(msg)
    def testCase5():
        try:
            assert('cs_recent_average' in globals()), "You do not have a DataFrame called `cs_recent_average`."
            assert('cs_old_average' in globals()), "You do not have a DataFrame called `cs_old_average`."
            assert('stat_recent_average' in globals()), "You do not have a DataFrame called `stat_recent_average`."
            assert('stat_old_average' in globals()), "You do not have a DataFrame called `stat_old_average`."
            assert(cs_recent_average == df_cs_recent["Percentage of As"].mean()), "`cs_recent_average` was not calculated correctly"
            assert(cs_old_average == df_cs_old["Percentage of As"].mean()), "`cs_old_average` was not calculated correctly"
            assert(stat_recent_average == df_stat_recent["Percentage of As"].mean()), "`stat_recent_average` was not calculated correctly"
            assert(stat_old_average == df_stat_old["Percentage of As"].mean()), "`stat_old_average` was not calculated correctly"
            print("Test Passed: \u2714")
        except AssertionError as msg:
            print("-"*10 + " ERROR " + "-"*10)
            print(msg)