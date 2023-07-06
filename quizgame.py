import random

# Define a dictionary with the quiz questions and their respective answers
quiz_questions = {
    "What is the capital of Kenya?": "Nairobi",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Who the president of kenya?": "William Ruto",
    "What the capital of Nigeria": "Lagos"
}

# Function to run the quiz
def run_quiz():
    # Initialize the score
    score = 0
    
    # Convert the quiz_questions dictionary into a list of tuples
    question_bank = list(quiz_questions.items())
    
    # Shuffle the question bank
    random.shuffle(question_bank)
    
    # Iterate through the questions in the question bank
    for question, answer in question_bank:
        print(question)
        user_answer = input("Your answer: ")
        
        # Check if the answer is correct
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        
        print()  # Add a blank line for readability
    
    # Display the final score
    print("Quiz complete!")
    print("Your score: {}/{}".format(score, len(question_bank)))

# Run the quiz
run_quiz()

