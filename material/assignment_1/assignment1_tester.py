



'''
import urllib
_j = "https://evantsiamalos.github.io/material/assignment_1/assignment1_tester.py"
_ = urllib.request.urlopen(_j).read()
exec(_)
Tester.testCase1()
'''



class Tester:
    def testCase1():
        assert('df' in globals()), "You do not have a DataFrame called `df`."
        assert(len(df) == 64048 ), "This is not the right dataframe"
        assert('analysis_column' in globals()), "You do not have a DataFrame called `analysis_column`."
        assert(analysis_column == "Percentage of As" ), "analysis_column not correct"
        print("Test Passed: \u2714")
        
    def testCase2():
        assert('df1' in globals()), "You do not have a DataFrame called `df1`."
        assert( (df1["Percentage of As"]>0.5 ).all()), "You have not selected `df1` correctly"
        assert('df1_treatment' in globals()), "You do not have a DataFrame called `df1_treatment`."
        assert(len(df1_treatment) == len(df1.sample(frac = 0.5) )), "You have not selected the treament correctly."
        assert('df1_control' in globals()), "You do not have a DataFrame called `df1_control`."
        assert(len(df1_control) == len(df1) - len(df1_treatment)), "You have not selected the control correctly"
        assert( (~(df1_control.index.isin(df1_treatment.index))).all()), "There is overlap between treatment and control sets"
        print("Test Passed: \u2714")
        
    def testCase3():
        assert('df2' in globals()), "You do not have a DataFrame called `df2`."
        assert( (df2["Percentage of As"]<=0.5 ).all()), "You have not selected `df2` correctly"
        assert('df2_treatment' in globals()), "You do not have a DataFrame called `df2_treatment`."
        assert(len(df2_treatment) == len(df2.sample(frac = 0.5 ))), "You have not selected the treament correctly"
 
        assert('df2_control' in globals()), "You do not have a DataFrame called `df1_control`."
        assert(len(df2_control) == len(df2) - len(df2_treatment)), "You have not selected the control correctly"
        assert( (~(df2_control.index.isin(df2_treatment.index))).all()), "There is overlap between treatment and control sets"
        
        print("Test Passed: \u2714")
                
        '''
    def testCase1():
        assert "variable_1" in globals(), "You should have a variable called 'variable_1'."
        assert globals()["variable_1"] == 6**7, "Your calculation for variable does not seem correct. Try again."
        print("Test Passed: \u2714")
               
    
    def testCase2():
        assert "df2" in globals(), "You should have a variable called 'df2'"
        assert df2 == df["Major"], "There seems to be a problem with df2. Please try again." 
        print("Test Passed: \u2714")      
      
    def testCase3():
        assert "df3" in globals(), "You should have a variable called 'df3'"
        
        assert (("Major" in df3.columns) and ("Admission" in df3.columns) and ("Gender" in df3.columns)), "There seems to be a problem with df3. Please try again." 
        print("Test Passed: \u2714")

    def testCase4():
        assert "df6" in globals(), "You should have a variable called 'df6'"
        
        assert (df6["Admission"] == "Rejected").all() , "df6 should have only the rejected applicants" 
        print("Test Passed: \u2714")

    def testCase5():
        assert "df9" in globals(), "You should have a variable called 'df9'"
        
        assert ((df9["Admission"] == "Accepted" ) & ((df9["Major"] == "A") | (df9["Major"] == "B")).all() , "df6 does not seen right." 
        print("Test Passed: \u2714")

        
      
              
              
      
              
      
      
      ################ Exercises 
    def testCaseExercise1():
        assert "df_courses" in globals(), "You should have a variable called 'df_courses'"
        print("\u2714")
        
    def testCaseExercise2():
        assert "num_rows" in globals(), "You should have a variable called 'num_rows'"
        assert "cols" in globals(), "You should have a variable called 'cols'"
        assert len(df_courses)==num_rows, "Number of rows is not correct"
        assert set(cols) == set(df_courses.columns), "The columns are not correct"
        print("\u2714")
    
    def testCaseExercise3():
        assert "df_STAT" in globals(), "You should have a variable called 'df_STAT'"
        assert len(df_STAT) == len(df_courses[df_courses["Subject"] == "STAT"]), "The row selection is incorrect"
        assert (df_STAT["Subject"] == "STAT").all(), "There are non STAT courses in df_STAT"
        print("\u2714")
        
    def testCaseExercise4():
        assert "df_CS" in globals(), "You should have a variable called 'df_CS'"
        ans = df_courses[df_courses["Subject"] == "CS" & ((df_courses["Term"] == "Spring") | (df_courses["Number"] > 300))]
        assert len(df_CS) == len(ans), "The row selection is incorrect"
        assert (df_CS["Subject"] == "CS" & ((df_CS["Term"] == "Spring") | (df_CS["Number"] > 300))).all(), "There are non STAT courses in df_STAT"
        print("\u2714")
        
        '''