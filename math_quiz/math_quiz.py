import random


def random_int(min, max):
    """
    Random integer in the range (min, max).
    Args:
        min (int): lower limit of the generated number
        max (int): upper limit of the generated number
    returns:
        random integer in the range (min, max).
    Examples:
        >>> random_int(3,8)
        5
        >>> random_int(0,10)
        9
    """
    return random.randint(min, max)

def random_operation():
    """
    chooses a random operation among addition, subtracttion and multiplication
    returns:
        random string from the list ['+', '-', '*']
    Examples:
        >>> random_operation()
        +
        >>> random_operation()
        *
    """
    return random.choice(['+', '-', '*'])

def perform_operation(int1, int2, operator):
    """
    performs one of three math operations and returns both the operation being performed as a string and the result.
    Args:
        int1 (int): first integer
        int2 (int): second integer
        operator (str): one of three math operator '+', '-', '*'
    returns:
        tuple:
            - output_string (str): string depicting the operation being performed
            - result (int): result of the performed operation
    Examples:
        >>> perform_operation(3, 4, '+')
        ('3 + 4', 7)        
        >>> perform_operation(3, 3, '*')
        ('3 * 3', 9) 
    """
    output_string = f"{int1} {operator} {int2}"
    if operator == '+': 
        result = int1 + int2
    elif operator == '-': 
        result = int1 - int2
    else: 
        result = int1 * int2
    return output_string, result

def math_quiz():
    """
    Runs a math quiz game where the user answers randomly generated math questions.

    The quiz asks the user a series of basic math problems and the user provides answers. 
    There are several rounds.

    Each round, the game:
        - Generates two random integers within specified ranges.
        - Selects a random mathematical operation.
        - Presents a math problem based on these values.
        - Prompts the user for an answer, comparing it with the correct answer. if the user input is not a valid int, keeps asking. 
        - Awards a point for each correct response and displays the correct answer if the user is incorrect.

    Finally, the user's total score at the end of the game is shown.

    Args:
        None

    Returns:
        None

    Example:
        Welcome to the Math Quiz Game!
        You will be presented with math problems, and you need to provide the correct answers.

        Question: 6 - 1
        Your answer: 5
        Correct! You earned a point.

        Question: 7 - 4
        Your answer: 3
        Correct! You earned a point.

        Question: 5 + 4
        Your answer: 2
        Wrong answer. The correct answer is 9.

        Game over! Your score is: 2/3
        
    """
    points = 0
    number_of_rounds = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(number_of_rounds):
        #picks two numbers and one operator at random using previously defined functions
        int1 = random_int(1, 10); 
        int2 = random_int(1, 5); 
        operator = random_operation()

        #prepares the problem to show the user and calculates the answer
        PROBLEM, ANSWER = perform_operation(int1, int2, operator)

        print(f"\nQuestion: {PROBLEM}")

        # while loop with try-except used to force the user to input valid int as answer 
        while True:
            try:
                useranswer = int(input("Your answer: "))
                if useranswer == ANSWER:
                    print("Correct! You earned a point.")
                    points += 1
                else:
                    print(f"Wrong answer. The correct answer is {ANSWER}.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    print(f"\nGame over! Your score is: {points}/{number_of_rounds}")

if __name__ == "__main__":
    math_quiz()
