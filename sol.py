"""
Implementation of basic go game with bfs subroutine.
"""
queue = []
COUNT = 0
visited = set()

class Game:
  def __init__(self):
    self.player = "R" # first turn is always Red player
    self.grid = []
    game_size = 9 # can extend this later
    for row in range(game_size):
      self.grid.append(["+" for space in range(game_size)])

  def show(self):
    """display game to stdout"""
    result = ""
    for row in self.grid:
      result += "".join(row) + "\n"
    print(result)

  def pass_turn(self):
    """change the current player without changing the board"""
    if self.player == "R":
      self.player = "G"
    else:
      self.player = "R"

  def get_square(self, x, y):
    """returns value of position on the board.
    Helps avoid thinking about the game datastructure"""
    return self.grid[y][x]

  def set_square(self, x, y):
    self.grid[y][x] = self.player
    
  def place_stone(self, x, y):
    """computes a game turn,
    returns bool False if stone failed to be placed"""
    square = self.get_square(x, y)
    if square == "+":
      self.set_square(x, y)
      self.pass_turn()
      return True
    else:
      return False

  def get_territory(self, x, y):
    """returns the number of contiguous squares with the
    red color. Algorithm is breadth first search.
    This method is NOT reentrant."""
    global COUNT
    visited.add((x, y))
    color = self.get_square(x,y)
    if color != "R":
      return False
    COUNT += 1 # square is red
    if x > 0:
      new_square = (x-1, y)
      if new_square not in visited and new_square not in queue:
        queue.append(new_square)
    if x < 8:
      new_square = (x+1, y)
      if new_square not in visited and new_square not in queue:
        queue.append(new_square)
    if y > 0:
      new_square = (x, y-1)
      if new_square not in visited and new_square not in queue:
        queue.append(new_square)
    if y < 8:
      new_square = (x, y+1)
      if new_square not in visited and new_square not in queue:
        queue.append(new_square)
    while queue:
      item = queue.pop()
      self.get_territory(item[0], item[1])
    return COUNT
    

g = Game()
print(f"game {g}")
g.show()

# make red 'L'
g.place_stone(8,0)
g.pass_turn()
g.place_stone(7,0)
g.pass_turn()
g.place_stone(7,1)
g.show()

g.place_stone(0,8)
g.show()

# make bigger red area for bfs
g.place_stone(6,0)
g.pass_turn()
g.place_stone(5,0)
g.pass_turn()
g.place_stone(6,1)
g.pass_turn()
g.place_stone(5,1)
g.pass_turn()
g.place_stone(4,1)
g.pass_turn()
g.place_stone(5,2)
g.pass_turn()
g.place_stone(4,2)
g.pass_turn()
g.place_stone(5,3)
g.pass_turn()
g.show()

# print(f"territory {g.get_territory(0,0)}")
print(f"territory {g.get_territory(8,0)}")
