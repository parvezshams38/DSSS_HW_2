import unittest
from math_quiz import random_int, random_operation, perform_operation


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation(self):
        # test if random operation is from the list ["+","-","*"]
        for _ in range(100):
             rand_op = random_operation()
             self.assertTrue(rand_op=="+" or rand_op=="-" or rand_op=="*")

    def test_perform_operation(self):
        # test if perform_operation() works properly 
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 1, '-', '3 - 1', 2),
                (3, 1, '*', '3 * 1', 3),
                (4, 5, '*', '4 * 5', 20),
                (9, 0, '+', '9 + 0', 9),                
                (9, 0, '-', '9 - 0', 9),
                (9, 0, '*', '9 * 0', 0),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                self.assertTrue((expected_problem,expected_answer) == (perform_operation(num1,num2,operator)))
                pass

if __name__ == "__main__":
    unittest.main()
