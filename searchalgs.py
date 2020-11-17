from setup import *
import heapq


def uniform_cost_search(problem):
    node = NodeU(problem.init_state)
    return optimal_search(node, problem)


def a_star_search(problem):
    node = NodeA(problem.init_state, heuristic=problem.h(problem.init_state))
    return optimal_search(node, problem)


def optimal_search(node, problem):
    frontier = [node]
    heapq.heapify(frontier)
    expanded = [problem.init_state]
    while frontier:
        current = heapq.heappop(frontier)
        if problem.goal_test(current.state):  # goal has been found
            return current
        if current in expanded:
            continue
        children = current.expand(problem)  # expand child
        expanded.append(current)
        for i in children:
            if i not in expanded:
                heapq.heappush(frontier, i)
    return Node(0, None, None)  # if frontier is empty, no solution
