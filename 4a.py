goal = [[1,2,3],[4,5,6],[7,8,0]]

# Display board
def display(state):
    for row in state:
        print(row)
    print()

# Check goal state
def is_goal(state):
    return state == goal

# Find blank position
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate successors
def successors(state):
    x, y = find_zero(state)
    moves = []
    dirs = [("Up",-1,0),("Down",1,0),("Left",0,-1),("Right",0,1)]

    for name, dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [row[:] for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            moves.append((name, new))

    return moves


# Test 4(a)
initial = [[1,2,3],[4,0,6],[7,5,8]]

print("Initial State:")
display(initial)

print("Successors:")
for move, s in successors(initial):
    print("Move:", move)
    display(s)

print("Is Goal?", is_goal(initial))