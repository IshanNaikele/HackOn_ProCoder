import pandas as pd
import tkinter as tk
import random

# Load the dataset
file_path = r"D:\Ishan\HackOn_ProCoder\Quiz app\Data\Countries.csv"
data = pd.read_csv(file_path)

# Keep only required columns
quiz_data = data[['country_name', 'capital_city', 'currency', 'landmarks']].dropna()

# Convert to dictionary for easy access
countries = quiz_data['country_name'].tolist()
capitals = quiz_data['capital_city'].tolist()
currencies = quiz_data['currency'].tolist()
landmarks = quiz_data['landmarks'].tolist()

quiz_dict = {
    'capital': dict(zip(countries, capitals)),
    'country_from_capital': dict(zip(capitals, countries)),
    'currency': dict(zip(countries, currencies)),
    'landmark': dict(zip(countries, landmarks)),
    'country_from_landmark': dict(zip(landmarks, countries))
}

# Track question count
question_count = 0
max_questions = 10

# Generate a new question
def generate_question():
    global correct_answer, question_count

    # End the game after 10 questions
    if question_count >= max_questions:
        question_label.config(text="🎉 Quiz Over! Well done!", font=("Arial", 18, "bold"))
        for btn in option_buttons:
            btn.pack_forget()  # Hide answer buttons
        result_label.config(text=f"You completed {max_questions} questions!", fg="blue")
        return
    
    # Increase question count
    question_count += 1

    # Randomly choose a question type
    question_types = [
        ("capital", "What is the capital of {country}?"),
        ("country_from_capital", "Which country has {capital} as its capital?"),
        ("currency", "What is the currency of {country}?"),
        ("landmark", "Which landmark is in {country}?"),
        ("country_from_landmark", "Which country has this landmark: {landmark}?")
    ]
    
    question_type, question_template = random.choice(question_types)

    if question_type == "capital":
        question_country = random.choice(countries)
        correct_answer = quiz_dict[question_type][question_country]
        question_text = question_template.format(country=question_country)
        
    elif question_type == "country_from_capital":
        question_capital = random.choice(capitals)
        correct_answer = quiz_dict[question_type][question_capital]
        question_text = question_template.format(capital=question_capital)
        
    elif question_type == "currency":
        question_country = random.choice(countries)
        correct_answer = quiz_dict[question_type][question_country]
        question_text = question_template.format(country=question_country)
        
    elif question_type == "landmark":
        question_country = random.choice(countries)
        correct_answer = quiz_dict[question_type][question_country]
        question_text = question_template.format(country=question_country)
        
    else:  # country_from_landmark
        question_landmark = random.choice(landmarks)
        correct_answer = quiz_dict[question_type][question_landmark]
        question_text = question_template.format(landmark=question_landmark)

    # Get 3 wrong answers
    all_answers = list(set(quiz_dict[question_type].values()))
    wrong_answers = random.sample([ans for ans in all_answers if ans != correct_answer], 3)
    options = wrong_answers + [correct_answer]
    random.shuffle(options)

    # Update GUI
    question_label.config(text=f"Question {question_count}/{max_questions}: {question_text}")
    for i, btn in enumerate(option_buttons):
        btn.config(text=options[i], command=lambda ans=options[i]: check_answer(ans))

# Function to check answer
def check_answer(answer):
    if answer == correct_answer:
        result_label.config(text="✅ Correct! Moving to next question...", fg="green")
    else:
        result_label.config(text="❌ Wrong! Try again.", fg="red")

    root.after(2000, generate_question)

# Set up GUI
root = tk.Tk()
root.title("Geography Quiz")

question_label = tk.Label(root, text="", font=("Arial", 16))
question_label.pack(pady=10)

option_buttons = []
for _ in range(4):
    btn = tk.Button(root, text="", font=("Arial", 14), width=20)
    btn.pack(pady=5)
    option_buttons.append(btn)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

generate_question()  # Start the first question
root.mainloop()
