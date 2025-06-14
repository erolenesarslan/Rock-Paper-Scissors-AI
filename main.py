import tkinter as tk
import random
from collections import Counter

choices = ['rock', 'paper', 'scissors']
user_history = []
user_score = 0
bot_score = 0

def predict_user_move():
    if not user_history:
        return random.choice(choices)
    most_common = Counter(user_history).most_common(1)[0][0]
    if most_common == 'rock':
        return 'paper'
    elif most_common == 'paper':
        return 'scissors'
    elif most_common == 'scissors':
        return 'rock'

def play(user_choice):
    global user_score, bot_score

    user_history.append(user_choice)
    bot_choice = predict_user_move()
    result = ""

    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (
        (user_choice == 'rock' and bot_choice == 'scissors') or
        (user_choice == 'paper' and bot_choice == 'rock') or
        (user_choice == 'scissors' and bot_choice == 'paper')
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Bot wins!"
        bot_score += 1

    result_label.config(text=f"Bot chose: {bot_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Bot: {bot_score}")

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors AI")
root.geometry("400x300")
root.resizable(False, False)

title = tk.Label(root, text="Choose your move", font=("Arial", 16))
title.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

rock_btn = tk.Button(buttons_frame, text="🪨 Rock", width=12, command=lambda: play('rock'))
paper_btn = tk.Button(buttons_frame, text="📄 Paper", width=12, command=lambda: play('paper'))
scissors_btn = tk.Button(buttons_frame, text="✂️ Scissors", width=12, command=lambda: play('scissors'))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score - You: 0 | Bot: 0", font=("Arial", 12))
score_label.pack()

root.mainloop()
