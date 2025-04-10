#Function to ask a question
def ask_question(question,correct_answer):
    answer = input(question).strip().lower() #convert answer to lowercase letters
    if answer==correct_answer.lower(): #ignore capital letters 
        print("Correct!")
    else:
        print("Wrong")

# List of European countries and capitals
questions= [
    ("What is the capital of France?","Paris"),
    ("What is the capital of United Kingdom?","London"),
    ("What is the capital of Belgium?","Brussels"),
    ("What is the capital of Greece?","Athens"),
    ("What is the capital of Spain?","Madrid"),
    ("What is the capital of Italy?","Rome"),
    ("What is the capital of Hungary?","Budapest"),
    ("What is the capital of Germany?","Berlin"),
    ("What is the capital of Sweden?","Stockholm"),
    ("What is the capital of Netherlands?","Amsterdam"),
]

# Check each question and ask for answer
for question, correct_answer in questions:
    ask_question(question, correct_answer)
