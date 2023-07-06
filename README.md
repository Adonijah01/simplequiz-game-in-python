Quiz Game

This is a simple quiz game implemented in Python. It asks a series of questions and checks the user's answers. The questions are stored in a dictionary, and the quiz randomly shuffles the questions before presenting them to the user. The user's score is displayed at the end of the quiz.
Requirements

    Python 3.x

How to Run

    Clone the repository:

    bash

git clone https://github.com/your-username/quiz-game.git

Navigate to the project directory:

bash

cd quiz-game

Run the script:

bash

    python quiz_game.py

Quiz Questions

The quiz questions and their respective answers are stored in a dictionary called quiz_questions. You can modify or extend this dictionary to include your own questions.

python

quiz_questions = {
    "What is the capital of Kenya?": "Nairobi",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Who is the president of Kenya?": "William Ruto",
    "What is the capital of Nigeria?": "Lagos"
}

How It Works

    The run_quiz() function is defined to run the quiz.
    The function initializes the score and converts the quiz_questions dictionary into a list of tuples called question_bank.
    The question_bank is shuffled randomly using the random.shuffle() function.
    The function iterates through each question in the question_bank.
    It displays the question to the user and waits for their answer.
    The user's answer is checked against the correct answer, ignoring case sensitivity.
    If the answer is correct, the user's score is incremented.
    At the end of the quiz, the final score is displayed.
