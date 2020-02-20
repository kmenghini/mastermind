import random

class Row:
  def __init__(self, values):
    self.values = values

  def __str__(self):
    printed_row = ''
    for value in self.values:
      printed_row += str(value)

    return printed_row
