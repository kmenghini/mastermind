import random
from row import Row

class Game:
  def __init__(self):
    pass

  def __str__(self):
    pass

  def get_secret_code(self):
    values = []
    for n in range(4):
      values.append(str(random.randint(1, 8)))
    secret_code = Row(values)
    return secret_code