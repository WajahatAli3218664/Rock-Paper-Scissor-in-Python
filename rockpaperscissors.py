# Topic: Project 4 In Python Quarter 3
# Instructor: Wajahat Ali
# 🗿 (Rock) | 📄 (Paper) | ✂️ (Scissors) Game

import random

# Game choices
choices = ["rock", "papers", "scissors"]

# Player choice
player_choice = input("Enter rock, paper, or scissors: ").lower()

# Validate player input
if player_choice not in choices:
    print("❌ Invalid choice! Please enter rock, paper, or scissors.")
else:
    # Computer choice
    computer_choice = random.choice(choices)

    print(f"\n🧑 Player's Choice: {player_choice} | 🤖 Computer's Choice: {computer_choice}")

    # Winner decision
    if player_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print(f"🎉 Player wins! {player_choice} beats {computer_choice}")
    else:
        print(f"💔 Computer wins! {computer_choice} beats {player_choice}")
