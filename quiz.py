import pandas as pd
import tkinter as tk
import random

# Load the dataset
data = pd.read_csv("Data/Countries.csv")  # Ensure the file path is correct
quiz_data = data[['country_name', 'capital_city']].dropna()

# Convert to dictionary for easy access
countries = quiz_data['country_name'].tolist()
capitals = quiz_data['capital_city'].tolist()
quiz_dict = dict(zip(countries, capitals))

# Function to generate a new question
def generate_question():
    global correct_answer
    question_country = random.choice(countries)
    correct_answer = quiz_dict[question_country]

    # Get 3 wrong answers
    wrong_answers = random.sample([cap for cap in capitals if cap != correct_answer], 3)
    options = wrong_answers + [correct_answer]
    random.shuffle(options)

    # Update GUI elements
    question_label.config(text=f"What is the capital of {question_country}?")
    for i, btn in enumerate(option_buttons):
        btn.config(text=options[i], command=lambda ans=options[i]: check_answer(ans))

# Function to check the answer
def check_answer(answer):
    if answer == correct_answer:
        result_label.config(text="✅ Correct! Moving to next question...", fg="green")
        root.after(2000, generate_question)  # Load new question after 2 seconds
    else:
        result_label.config(text="❌ Wrong! Try again.", fg="red")

# Set up GUI
root = tk.Tk()
root.title("Capital Quiz")

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
