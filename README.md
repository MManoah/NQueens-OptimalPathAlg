# NQueens-OptimalPathAlg

The N-queens puzzle is the problem of placing N queens on an N x N chessboard such that no two queens attack each other. This finds a solution to an N-Queens problem using either Uniform-Cost search or A* search.

The indexes of the list will represent columns on a chessboard (0 -> N-1) while the numbers in each index will represent the row of the queen location in that column (0 -> N-1).


## The Two Algorithms

### A*

The A* algorithm uses a combination of heuristic values and the path cost in order to find an optimal solution. This algorithm is significantly faster than Uniform-Cost.

f(n) = g(n) + h(n) where:

g(n) = path cost

h(n) = heuristic (estimated cost to the goal)

### Uniform-Cost

The Uniform-Cost algorithm uses the path cost in order to find an optimal solution.

f(n) = g(n) where:

g(n) = path cost

## Example

Here is a solution for the 8-Queens problem using the two algorithms

![](https://i.gyazo.com/49f476cd5a6d92b654daf419dfd1303f.png)

Here would be the board configuration for A*

![](https://i.gyazo.com/b9897a9733b8f3e706c85a92a33a77f0.png)


## Built With

* Python

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
