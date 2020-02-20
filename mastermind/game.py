import random
from row import Row

class Game:
  def __init__(self):
    self.rows = []

  def __str__(self):
    game_view = '\nYour Guesses:\n'
    for row in self.rows:
      game_view += (str(row) + '\n')
    return game_view

  def get_secret_code(self):
    values = []
    for n in range(4):
      values.append(str(random.randint(1, 8)))
    secret_code = Row(values)
    return secret_code

  def add_row(self, guess):
    row = Row(list(guess))
    self.rows.append(row)
