class PuzzleBoard:
    def __init__(self, state):
        self.state = state
        self.goal = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 0]]

    def display(self):
        for row in self.state:
            print(row)
        print()

    def is_goal(self):
        return self.state == self.goal

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def copy(self):
        return [row[:] for row in self.state]

    def generate_successors(self):
        successors = []
        x, y = self.find_blank()

        moves = {
            "Up": (x - 1, y),
            "Down": (x + 1, y),
            "Left": (x, y - 1),
            "Right": (x, y + 1)
        }

        for move, (new_x, new_y) in moves.items():
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = self.copy()
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                successors.append((move, PuzzleBoard(new_state)))

        return successors