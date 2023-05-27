class Tester:

    def tesstCase1():
        assert "variable_1" in globals(), "you should name the variable as variable_1"
        assert globals()["variable_1"] == 6**7, "your_calculation does not seem correct"
        