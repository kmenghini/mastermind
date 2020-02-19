import random

class Row:
  def __init__(self, values):
    self.values = values

  def __str__(self):
    printed_row = ''
    for value in self.values:
      printed_row += str(value)

    return printed_row

  def get_secret_code(self):
    secret_code = []
    for n in range(4):
      secret_code.append(random.randint(1, 8))
    return secret_code