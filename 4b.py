import heapq

goal = [[1,2,3],[4,5,6],[7,8,0]]

# Heuristic: Manhattan Distance
def h(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x = (val-1)//3
                y = (val-1)%3
                dist += abs(i-x) + abs(j-y)
    return dist

# Find blank
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighbors
def neighbors(state):
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

# A* Algorithm
def astar(start):
    pq = []
    heapq.heappush(pq, (h(start), 0, start, [(None, start)]))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        visited.add(str(state))

        for move, nxt in neighbors(state):
            if str(nxt) not in visited:
                heapq.heappush(pq, (g+1+h(nxt), g+1, nxt, path+[(move, nxt)]))

    return None

# Find which tile moved
def find_moved_tile(prev, curr):
    for i in range(3):
        for j in range(3):
            if prev[i][j] != 0 and curr[i][j] == 0:
                return prev[i][j]

# Test 4(b)
start = [[1,2,3],[4,0,6],[7,5,8]]

result = astar(start)

print("Solution Steps:\n")

for i in range(1, len(result)):
    move, state = result[i]
    prev_state = result[i-1][1]

    tile = find_moved_tile(prev_state, state)

    print(f"Move {i}: Move {tile} {move}")
    for row in state:
        print(row)
    print()