import heapq
from puzzle import PuzzleBoard   # Import Part (a)

# Heuristic: Manhattan Distance
def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def a_star(initial_state):
    start = PuzzleBoard(initial_state)

    open_list = []
    counter = 0
    heapq.heappush(open_list, (0, counter, start))

    came_from = {}
    g_cost = {str(start.state): 0}

    while open_list:
        _, _, current = heapq.heappop(open_list)

        if current.is_goal():
            return reconstruct_path(came_from, current)

        for move, neighbor in current.generate_successors():
            new_cost = g_cost[str(current.state)] + 1

            if str(neighbor.state) not in g_cost or new_cost < g_cost[str(neighbor.state)]:
                g_cost[str(neighbor.state)] = new_cost

                priority = new_cost + manhattan_distance(neighbor.state, current.goal)

                counter += 1
                heapq.heappush(open_list, (priority, counter, neighbor))

                came_from[str(neighbor.state)] = (current, move)

    return None

def reconstruct_path(came_from, current):
    path = []
    while str(current.state) in came_from:
        parent, move = came_from[str(current.state)]
        path.append((move, current))
        current = parent
    path.reverse()
    return path


# ----------- MAIN -------------

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    print("Initial Board:\n")
    board = PuzzleBoard(initial_state)
    board.display()

    print("Solving using A*...\n")

    solution = a_star(initial_state)

    if solution:
        step = 1
        for move, state in solution:
            print(f"Move {step}: {move}")
            state.display()
            step += 1
    else:
        print("No solution found.")