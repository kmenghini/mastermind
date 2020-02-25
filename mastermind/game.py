import random
from row import Row

class Game:
  def __init__(self):
    self.rows = []

  def __str__(self):
    game_view = '\n\n--------------\nYour Guesses:\n'
    for row in self.rows:
      game_view += (str(row) + '\n')
    return game_view

  def get_secret_code(self):
    values = []
    for n in range(4):
      values.append(str(random.randint(1, 8)))
    self.secret_code = Row(values)
    # doesn't need to return anything
    return self.secret_code

  def add_row(self, new_row):
    self.rows.append(new_row)

  def is_correct_solution(self, new_row):
    return self.secret_code.values == new_row.values

  def get_number_of_rows(self):
    return len(self.rows)
