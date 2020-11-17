from searchalgs import *

board = NQueensProblem(8)  # A* can solve up to around 15 queens fast
a_star = a_star_search(board)
uniform_cost = uniform_cost_search(board)
print('A*: ' + str(a_star.solution()))
print('Uniform-Cost: ' + str(uniform_cost.solution()))
