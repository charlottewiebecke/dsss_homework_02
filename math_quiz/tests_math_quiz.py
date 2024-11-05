import unittest
from math_quiz import create_random_integer, random_operator, generate_problem_and_answer


class TestMathGame(unittest.TestCase):

    def test_create_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = create_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if the selected operator is one of the expected operators
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test multiple times to ensure randomness
            operator = random_operator()
            self.assertIn(operator, operators)

    def test_generate_problem_and_answer(self):
        # Define test cases for generate_problem_and_answer
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            # Add additional test cases if needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem_and_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
