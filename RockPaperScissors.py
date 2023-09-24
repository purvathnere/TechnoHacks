import tkinter as tk
import random

name="Created by Purva Athnere"
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Scissors" and computer_choice == "Paper")
        or (player_choice == "Paper" and computer_choice == "Rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# player choice
def player_choice(choice):
    computer_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choices)

    result = determine_winner(choice, computer_choice)
    result_label.config(text=result)

    player_label.config(text=f"Your choice: {choice}")
    computer_label.config(text=f"Computer's choice: {computer_choice}")

# window
RockPaperScissors = tk.Tk()
RockPaperScissors.configure(bg="green")
RockPaperScissors.title('"Rock, Paper, Scissors "'+ name)

RockPaperScissors.geometry("500x500")

# labels
player_label = tk.Label(RockPaperScissors, text="Your choice: ", font=("Helvetica", 12),bg="green")
player_label.pack(pady=10)

computer_label = tk.Label(RockPaperScissors, text="Computer's choice: ", font=("Helvetica", 12),bg="green")
computer_label.pack()

result_label = tk.Label(RockPaperScissors, text="", font=("Helvetica", 16),bg="green")
result_label.pack()

choices = ["Rock", "Paper", "Scissors"]

for choice in choices:
    button = tk.Button(RockPaperScissors, text=choice, width=10, height=2, command=lambda c=choice: player_choice(c), bg="#5e77d1")
    button.pack(padx=10, pady=10) 

tk.Label(RockPaperScissors, text=name , fg="blue" ).pack(side="bottom")

RockPaperScissors.mainloop()
