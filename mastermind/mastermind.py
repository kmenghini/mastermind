from game import Game
from row import Row

playing = True

print("Let's Play Mastermind")
game = Game()
print("Creating secret code...")
# should not store solution
solution = game.get_secret_code()
# should not print solution
print(solution)

while playing:
  # take input guess
  guess = str(input("Enter your guess: "))
  new_row = Row(list(guess))

  if game.is_correct_solution(new_row):
    playing = False
    print("YOU WON in {} guesses!\n".format(
      game.get_number_of_rows()
    ))
    break
  # add to game
  game.add_row(new_row)
  print(game)

  # check row - returns count of black & white markers

