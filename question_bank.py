#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"), ("What is the chemical symbol for hydrogen", "H"), 
        ("What is the chemical symbol for oxygen?", "O2"),
        
    ],
    "Maths": [
        ("What is 2+2?", "0"), ("What is 6/3?", "2"), 
        ("What is 2x2?", "4"),
    ],
}

hints = {
    "Science": [
        ("What is the chemical symbol for water?", "what is included in the components of water"),
        ("What is the chemical symbol for hydrogen?", "Its in the name"),
        ("What is the chemical symbol for oxygen?", "its in the name too"), ],
        "Maths": [
        ("What is 2+2?", "add it"), ("What is 6/3?", "divide it"), 
        ("What is 2x2?", "multiply it"),
       
    ],
    
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    questionss = questions.get(category, [])
    ranq = random.choice(questionss)
    return ranq
    #------------------------
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    if player_answer==correct_answer:
        return True
    else:
        return False
    #------------------------
    #------------------------

#---------------------------------------

def remove_question(category, questions):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    if category in questions:
        qlis = questions[category]
        if questions in qlis:
            qlis.remove(questions)
    #------------------------
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    qtext, answer = question
    print(qtext)
    panswer = input("Your answer: ")
    return panswer
    #------------------------
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    if category in hints:
        hint = hints[category].get(question, "No hint")
        return hint
    else:
        return "No hints available for questions in this category."
    #------------------------
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    print("Incorrect answer. The correct answer is:", correct_answer)
    #------------------------
    #------------------------

#---------------------------------------




