import random

class Row:
  def __init__(self, values):
    self.values = values
    self.keys = {}

  def __str__(self):
    printed_row = ''
    for value in self.values:
      printed_row += str(value)

    printed_keys = ''
    if self.keys:
      printed_keys = str(self.keys)

    return '{} | {}'.format(printed_row, printed_keys)

  def add_keys_to_row(self, secret_code):
    guess_values = self.values
    code_values = secret_code.values
    black_count = 0
    white_count = 0
    checked_guess_values = [0, 0, 0, 0]
    checked_code_values = [0, 0, 0, 0]

    for index, value in enumerate(guess_values):
      if value == code_values[index]:
        black_count += 1
        checked_guess_values[index] = 1
        checked_code_values[index] = 1

    for i, guess_value in enumerate(guess_values):
      for j, code_value in enumerate(code_values):
        if not checked_code_values[j] and not checked_guess_values[i]:
          if guess_value == code_value:
            white_count += 1
            checked_guess_values[i] = 1
            checked_code_values[j] = 1


    self.keys = {
      'black': black_count,
      'white': white_count,
    }
