class Tester:

    def testCase1():
        assert "variable_1" in globals(), "You should have a variable called 'variable_1'."
        assert globals()["variable_1"] == 6**7, "Your calculation for variable does not seem correct. Try again."
    
    
    def testCase2():
        assert "df2" in globals(), "You should have a variable called 'df2'"
        assert df2 == df["Major"], "There seems to be a problem with df2. Please try again." 
      
      
    def testCase3():
        assert "df3" in globals(), "You should have a variable called 'df3'"
        
        assert (("Major" in df3.columns) and ("Admission" in df3.columns) and ("Gender" in df3.columns)), "There seems to be a problem with df3. Please try again." 
      
      
      
      ################ Exercises 
    def testCaseExercise1():
        print("\u2714")
        
    def testCaseExercise2():
        print("\u2714")
    
    def testCaseExercise3():
        print("\u2714")
        
    def testCaseExercise4():
        print("\u2714")
            
        
    