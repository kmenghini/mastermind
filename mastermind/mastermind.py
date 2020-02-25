from game import Game
from row import Row

playing = True

print("\nLet's Play Mastermind\n")
game = Game()
print("Creating secret code...\n")
game.get_secret_code()

while playing:
  guess = str(input("Enter your guess: "))

  if len(guess) == 4:
    new_row = Row(list(guess))
    new_row.add_keys_to_row(secret_code=game.secret_code)
    game.add_row(new_row)
    print(game)

    if game.is_correct_solution(new_row):
      playing = False
      print("\nYOU WON in {} guesses!\n".format(
        game.get_number_of_rows()
      ))
      break
