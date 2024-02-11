import tbutils
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
  def __init__(self, _id, name, date, harem, coins, count, unique, level, xp):
    self._id = _id
    self.name = name
    self.date = date
    self.harem = harem
    self.count = count
    self.unique = unique
    self.coins = coins
    self.level = level
    self.xp = xp

  def get_completion_rate(self):
    pass


class Group:
  def __init__(self, _id, title, photo, spawned, message_count, current, date):
    self._id = _id
    self.title = title
    self.photo = photo
    self.spawned = False
    self.message_count = message_count
    self.current = current
    self.date = date
    
  def get_top_users(self):
    pass