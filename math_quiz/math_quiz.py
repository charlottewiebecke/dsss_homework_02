import random


def create_random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value.
    
    Parameters:
        min_value: The minimum value for the random integer.
        max_value: The maximum value for the random integer.
        
    Returns:
        int: A random integer between min_value and max_value.
    """
    
    return random.randint(min_value, max_value)


def random_operator():
    """
    Selects a random operator out of ['+', '-', '*'].
    Returns:
        str: A random operator.
    """     
    
    return random.choice(['+', '-', '*'])


def generate_problem_and_answer(number1, number2, operator):
    """
    Generates a problem and computes the answer with the given operator.
    
    Parameters:
        number1: The first number in the problem.
        number2: The second number in the problem.
        operator: The operator to apply ('+', '-', or '*').
        
    Returns:
        tuple: A tuple containing the problem as a string and the correct answer as an int.
    """

    problem = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return problem, answer

def math_quiz():
    """
    Main function to run the Math Quiz Game.
    It presents the user with math problems and checks their answers.
    """
    score = 0
    total_questions = 5  # Set to an integer to fix the bug in the original code.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate two random numbers and a random operator.
        number1 = create_random_integer(1, 10)
        number2 = creaate_random_integer(1, 10) # converted to int
        operator = random_operator()

        # Generate problem and answer.
        problem, correct_answer = generate_problem_and_answer(number1, number2, operator)
        print(f"\nQuestion: {problem}")

        try:
            # Get user answer and convert to integer
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue  # Skip to the next question if input is invalid.

        # Check if the answer is correct.
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Display final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
