print("importato classi")

class Legend:
  def __init__(self, _id, name, skinline, role, image, sauce, guesses):
    self._id = _id
    self.name = name
    self.skinline = skinline
    self.role = role
    self.image = image
    self.sauce = sauce
    self.guesses = guesses


class User:
  def __init__(self, id, name, date, harem, coins, count, unique, level, xp):
    self.id = id
    self.name = name
    #self.date = get_date()
    self.harem = harem
    self.count = count
    self.unique = unique
    self.coins = coins
    self.level = level
    self.xp = xp

  def get_completion_rate(self):
    pass


class Group:
  def __init__(self, title, photo):
    self.title = title
    self.photo = photo

  def get_top_users(self):
    pass