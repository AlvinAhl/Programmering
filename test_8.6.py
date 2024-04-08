class Point:
    """Represents a point in 2D space."""

    def __init__(self, column=0, row=0):
        """Initialize a point with column and row coordinates."""
        self.column = column
        self.row = row

    def __eq__(self, other):
        """Check if two points are equal."""
        return self.column == other.column and self.row == other.row


class ShipPart:
    """Represents a part of a ship."""

    def __init__(self, point):
        """Initialize a ship part with a given point."""
        self.point = point
        self.hit = False

    def attack(self, point):
        """Attempt to hit the ship part."""
        if point == self.point:
            self.hit = True
            return True
        return False

    def is_hit(self):
        """Check if the ship part has been hit."""
        return self.hit


class Ship:
    """Represents a ship in the game."""

    def __init__(self, length=2, start_point=Point(0, 0), orientation='right'):
        """Initialize a ship with a given length, starting point, and orientation."""
        self.length = length
        self.hits = 0
        self.ship_parts = [ShipPart(Point(start_point.column + (i if orientation == 'right' else 0),
                                          start_point.row + (i if orientation == 'down' else 0)))
                           for i in range(length)]

    def attack(self, point):
        """Attempt to hit the ship."""
        for part in self.ship_parts:
            if part.attack(point):
                self.hits += 1
                return True
        return False

    def is_destroyed(self):
        """Check if the ship has been destroyed."""
        return self.hits == self.length


class Board:
    """Represents the game board."""

    def __init__(self, width=8, height=8):
        """Initialize a game board with a given width and height."""
        self.width = width
        self.height = height
        self.ships = []
        self.hits = []
        self.misses = []

    def add_ship(self, ship):
        """Add a ship to the board."""
        self.ships.append(ship)

    def attack(self, point):
        """Attempt to attack a ship at the given point."""
        for ship in self.ships:
            if ship.attack(point):
                self.hits.append(point)
                return True
        self.misses.append(point)
        return False

    def is_game_over(self):
        """Check if all ships have been destroyed."""
        return all(ship.is_destroyed() for ship in self.ships)

    def print(self):
        """Print the board."""
        for y in range(self.height):
            for x in range(self.width):
                point = Point(x, y)
                if point in self.hits:
                    print('X', end='')
                elif point in self.misses:
                    print('O', end='')
                else:
                    print('.', end='')
            print()


class Game:
    """Represents the game of Battleship."""

    def __init__(self, width, height):
        """Initialize the game with a given width and height."""
        self.board = Board(width, height)

    def add_ship(self, length, start_point, orientation):
        """Add a ship to the game board."""
        self.board.add_ship(Ship(length, start_point, orientation))

    def play(self):
        """Start the game."""
        while not self.board.is_game_over():
            self.board.print()
            try:
                column = int(input('Enter column: '))
                row = int(input('Enter row: '))
            except ValueError:
                print("Invalid input! Please enter integer values.")
                continue
            point = Point(column, row)
            if self.board.attack(point):
                print('Hit!')
            else:
                print('Miss!')
        self.board.print()
        print('Game over!')


game = Game(8, 8)
game.add_ship(3, Point(0, 0), 'right')
game.play()
