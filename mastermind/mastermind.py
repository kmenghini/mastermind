from game import Game

playing = True

print("Let's Play Mastermind")
game = Game()
print("Creating secret code...")
solution = game.get_secret_code()
print(solution)

# loop until correct
# take input guess
guess = str(input("Enter your guess: "))
# add row to the Game
game.add_row(guess)
print(game)
# check row and get count of black & white markers

