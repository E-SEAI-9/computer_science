import random

# Choices are stored in a tuple to keep them immutable
CHOICES = ("rock", "paper", "scissors")

while True:
    player = input("Choose Rock, Paper, or Scissors: ").strip().lower()

    if player not in CHOICES:
        print("That is not a valid choice. Try again.")
        continue

    computer = random.choice(CHOICES)

    print(f"You chose: {player.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")

	# The match(player, computer) bundles the player and computer variables into a temporary tuple to check both at the same time.
    match (player, computer):
        case _ if player == computer:
            print("It's a tie!")

		# Each case checks for a matching (player_choice, computer_choice) combination.
		# The pipe symbol (|) acts as "or" to check all winning scenarios at once.
        case ("rock", "scissors") | ("paper", "rock") | ("scissors", "paper"):
            print("You win!")
        case _:
            print("Computer wins!")

    again = input("Play again? (y/n): ").strip().lower()
    if again in ("n", "no"):
        print("Game over! Thanks for playing.")
        break