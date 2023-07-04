import math as m
tol = 1e-3

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
    def testExercise1():
        try:
            assert('answer_1' in globals()), "You do not have a variable called `answer_1`."
            assert answer_1 == 13/52 or m.isclose(answer_1 , 13/52,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)
                   
    def solution1():
        sol = '''
        Answer: 13/52
        There are 13 chances of drawing a club out of 52 possible cards. The probability of drawing a club is then 13/52.
        '''
        print(sol)
        
    def testExercise2():
        correct_ans = 3/8
        try:
            assert('answer_2' in globals()
                  ), "You do not have a variable called `answer_2`."
            assert answer_2 == correct_ans or m.isclose(answer_2 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution2():
        sol = '''
        Answer: 3/8
        On one 8-sided die, there are 3 chances of the die rolling a value greater or equal to 6 out of 8 possibilities. Then, the possibility of the die rolling a value greater or equal to 6 is 6/8.       '''
        print(sol)
        
    def testExercise3():
        correct_ans = 2/4
        try:
            assert('answer_3' in globals()
                  ), "You do not have a variable called `answer_3`."
            assert answer_3 == correct_ans or m.isclose(answer_3 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution3():
        sol = '''
        Answer: 2/4
        On one 4-numbered wheel, there are 2 chances of the wheel lands on an even value out of 4 possibilities. Then, the possibility of the wheel lands on an even value is 2/4.'''
        print(sol)
        
    def testExercise4():
        correct_ans = 52/64
        try:
            assert('answer_4' in globals()
                  ), "You do not have a variable called `answer_4`."
            assert answer_4 == correct_ans or m.isclose(answer_4 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution4():
        sol = f'''
        Answer: 52/64
        Spinning two 8-numbered wheels has 64 possible outcomes. 
        There are 28 chances of at least one wheel lands on a multiple of 3 out of 64 possible spins and 40 chances of the second value is greater than or equal to 4 out of 64 possible spins. 
        The two conditions are both true for 16 possible spins. 
        Since we are finding the probability of at least one wheel lands on a multiple of 3 OR the second value is greater than or equal to 4, 
        we can use the Addition Rule and add the individual probabilities together, 
        while subtracting the probability of both being true to avoid double counting. 
        Then the probability is (28 + 40 - 16)/64 = 52/64.'''
        print(sol)
        
        
        
        
    def testExercise5():
        correct_ans = 63/144
        try:
            assert('answer_5' in globals()
                  ), "You do not have a variable called `answer_5`."
            assert answer_5 == correct_ans or m.isclose(answer_5 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution5():
        sol = f'''
        Answer: 63/144
        Spinning two 12-numbered wheels has 144 possible outcomes. There are {2*3*12 - 9} chances of at least one wheel lands on a multiple of 4 out of 144 possible spins. Then the probability is 63/144.'''
        print(sol)
                                
    def testExercise6():
        correct_ans = 5/25
        try:
            assert('answer_6' in globals()
                  ), "You do not have a variable called `answer_6`."
            assert answer_6 == correct_ans or m.isclose(answer_6 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution6():
        sol = f'''
        Answer: 5/25
        Rolling two 5-sided dice has 25 possible outcomes. There are {5} chances of both dice having the same outcome. Then the probability is 5/25.'''
        print(sol)

        
    def testExercise7():
        correct_ans = (9+1)/36
        try:
            assert('answer_7' in globals()
                  ), "You do not have a variable called `answer_7`."
            assert answer_7 == correct_ans or m.isclose(answer_7 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution7():
        sol = f'''
        Answer: 10/36
        Rolling two 6-sided dice has 36 possible outcomes. 
        There are {9} chances of both dice having even numbers and 1 chance of both dice having the outcome 1. Those events are disjoint. 
        Then the probability is (9+1)/36 = 10/36.'''
        print(sol)
        
        
    def testExercise8():
        correct_ans = (13+13)/52
        try:
            assert('answer_8' in globals()
                  ), "You do not have a variable called `answer_8`."
            assert answer_8 == correct_ans or m.isclose(answer_8 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution8():
        sol = f'''
        Answer: {13+13}/{52} 
        There are {13} chances of drawing a spade and 13 chances of drawing a diamond. Those events are disjoint. 
        Then the probability is (13+13)/52 = 26/52.'''
        print(sol)

        
    def testExercise9():
        correct_ans = 1-(32*31*30)/(94*93*92)
        try:
            assert('answer_9' in globals()
                  ), "You do not have a variable called `answer_9`."
            assert answer_9 == correct_ans or m.isclose(answer_9 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution9():
        sol = f'''
        Answer: 1 -  (32*31*30) / (94 * 93 * 92)
        
        
        We use the complement rule: P(AT LEAST ONE student is a coffee drinker) = 1 - P(NONE of those 3 is a coffee drinker)
        
        In order to calculate P(NONE of those 3 is a coffee drinker) when choosing students without replacement we have:
        - First student: 32 chances for NOT COFFEE DRINKER out of 34 students
        - Second student: 31 chances for NOT COFFEE DRINKER out of 33 students (because we have already selected one)
        - Third student: 30 chances for NOT COFFEE DRINKER out of 32 students (because we have already selected two)
        
        So P(AT LEAST ONE student is a coffee drinker) = (32* 31*30)/(94*93*92)
        and the P(AT LEAST ONE student is a coffee drinker) = 1 - (32* 31*30)/(94*93*92)
        '''
        print(sol)

        
    def testExercise9():
        correct_ans = 1-(32*31*30)/(94*93*92)
        try:
            assert('answer_9' in globals()
                  ), "You do not have a variable called `answer_9`."
            assert answer_9 == correct_ans or m.isclose(answer_9 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution9():
        sol = f'''
        Answer: 1 -  (32*31*30) / (94 * 93 * 92)
        
        
        We use the complement rule: P(AT LEAST ONE student is a coffee drinker) = 1 - P(NONE of those 3 is a coffee drinker)
        
        In order to calculate P(NONE of those 3 is a coffee drinker) when choosing students without replacement we have:
        - First student: 32 chances for NOT COFFEE DRINKER out of 34 students
        - Second student: 31 chances for NOT COFFEE DRINKER out of 33 students (because we have already selected one)
        - Third student: 30 chances for NOT COFFEE DRINKER out of 32 students (because we have already selected two)
        
        So P(AT LEAST ONE student is a coffee drinker) = (32* 31*30)/(94*93*92)
        and the P(AT LEAST ONE student is a coffee drinker) = 1 - (32* 31*30)/(94*93*92)
        '''
        print(sol)

    def testExercise10():
        correct_ans = 1-(1/2)**3
        try:
            assert('answer_10' in globals()
                  ), "You do not have a variable called `answer_10`."
            assert answer_10 == correct_ans or m.isclose(answer_10 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution10():
        sol = f'''
        Answer: 1 -  (1/2)**3
        
        
        We use the complement rule: P(AT LEAST ONE question correct) = 1 - P(ALL questions incorrect).
        
    

        In order to calculate P(ALL questions incorrect) we do the following:
        
        - we write P(ALL questions incorrect) = 
            P(1st question incorrect AND 2nd question incorrect AND 3rd question incorrect)
        
        - Due to independence of the questions, we write
          P(1st Q incorrect AND 2nd Q incorrect AND 3rd Q incorrect) = 
          P(1st Q incorrect) * P(2nd Q incorrect) * P(3rd Q incorrect)
          
        - For each question, the probability of getting the wrong answer is 1/2
        
        - So P(1st Q incorrect AND 2nd Q incorrect AND 3rd Q incorrect) =
          (1/2) * (1/2) * (1/2) = (1/2)**3
        
        - and the probability P(AT LEAST ONE question correct) = 1 - (1/2)**3 
        
        '''
        print(sol)
     
    def testExercise11():
        correct_ans = 1-(2*13/52 - (13/52)*(12/51))
        try:
            assert('answer_11' in globals()
                  ), "You do not have a variable called `answer_11`."
            assert answer_11 == correct_ans or m.isclose(answer_11 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution11():
        sol = f'''
        Answer: 1-(13/52 + 13/52 - (13/52)*(12/51))
        
        
        We use the complement rule: P(BOTH cards are NOT diamonds) = 1 - P(AT LEAST ONE card is a diamond).
        
    

        In order to calculate P(AT LEAST ONE card is a diamond) we do the following:
        
        - we write P(AT LEAST ONE card is a diamond) = 
            P(1st card diamond OR 2nd card diamond)
        
        - We use the addition rule:
            P(1st card diamond OR 2nd card diamond) = 
            P(1st card diamond) + P(2nd card diamond) - P(Both cards diamonds)
            
            - P(1st card diamond) = 13/52
            - P(2nd card diamond) = 13/52
            
            - for P(Both cards diamonds), we have that for the first draw, we have
                13 choices out of 52 and for the second draw we have 12 choices out 
                of 51 (beacuse we have already taken a diamond out from the first draw).
                
                So  P(Both cards diamonds) = (13/52)(12/51)
      
        - Finally we put it together:
            P(BOTH cards are NOT diamonds) = 1 - (13/52 + 13/52 - (13/52)(12/51))
            
        '''
        print(sol)

        
     
    def testExercise12():
        correct_ans = 0.7*0.3*0.7*0.3
        try:
            assert('answer_12' in globals()
                  ), "You do not have a variable called `answer_12`."
            assert answer_12 == correct_ans or m.isclose(answer_12 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution12():
        sol = f'''
        Answer:  0.3 * 0.7 * 0.3 * 0.7
        
        These are four independent tosses, so we use the multiplication rule.
        For each coin flip, P(H) = 0.7 and P(T) = 0.3.
        
        '''
        print(sol)
        
        
    def testExercise13():
        correct_ans = (1/5)**3
        try:
            assert('answer_13' in globals()
                  ), "You do not have a variable called `answer_13`."
            assert answer_13 == correct_ans or m.isclose(answer_13 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution13():
        sol = f'''
        Answer:  (1/5)**3
        
        These are 3 independent questions, so we use the multiplication rule.
        For each question, P(right answer) = 1/5.
        
        '''
        print(sol)
        
    def testExercise14():
        correct_ans = 1 - (14/20)**3
        try:
            assert('answer_14' in globals()
                  ), "You do not have a variable called `answer_14`."
            assert answer_14 == correct_ans or m.isclose(answer_14 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution14():
        sol = f'''
        Answer:  1 - (14/20)**3
        
        We use the complement rule: P(at least one red) = 1 - P(all three tickets are NOT red)
        
        For P(all three tickets are NOT red) = P(1st not red AND 2nd not red AND 3rd not red)
        we use the multiplication rule: 
        
        
        P(1st not red AND 2nd not red AND 3rd not red) = 
        P(1st not red) * P(2nd not red) * P(3rd not red) =
        (14/20) * (14/20)* (14/20) = (14/20)**3 
        '''
        print(sol)
        
    def testExercise15():
        correct_ans = 1 - (14/20)**3
        try:
            assert('answer_14' in globals()
                  ), "You do not have a variable called `answer_14`."
            assert answer_14 == correct_ans or m.isclose(answer_14 , correct_ans,rel_tol= tol), "Your calculation is not correct"
            
            print(f"\N{PARTY POPPER} Correct Answer! \N{PARTY POPPER}")
        except AssertionError as msg:
            print(f'{bcolors.FAIL} ---------- ERROR ---------- {bcolors.ENDC}')
            print(msg)

    def solution15():
        sol = f'''
        Answer:  1 - (14/20)**3
        
        We use the complement rule: P(at least one red) = 1 - P(all three tickets are NOT red)
        
        For P(all three tickets are NOT red) = P(1st not red AND 2nd not red AND 3rd not red)
        we use the multiplication rule: 
        
        
        P(1st not red AND 2nd not red AND 3rd not red) = 
        P(1st not red) * P(2nd not red) * P(3rd not red) =
        (14/20) * (14/20)* (14/20) = (14/20)**3 
        '''
        print(sol)