import random 

choices = ['rock', 'paper', 'scissors']

your_choice = int(input('Choose 1 for rock, 2 for paper, or 3 for scissors: '))
print(f"You chose {choices[your_choice - 1]}")

computer_choice = random.choice(choices)
print(f"Computer picks {computer_choice}")

if your_choice == 1 and computer_choice == 'paper':
  print("You lose")
elif your_choice == 1 and computer_choice == 'scissors':
  print("You win")
elif your_choice == 2 and computer_choice == 'rock':
  print("You win")
elif your_choice == 2 and computer_choice == 'scissors':
  print("You lose")
elif your_choice == 3 and computer_choice == 'rock':
  print("You lose")
elif your_choice == 3 and computer_choice == 'paper':
  print("You win")
elif your_choice == computer_choice:
  print("It's a draw")