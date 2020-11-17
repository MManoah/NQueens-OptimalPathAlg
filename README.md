# NQueens-OptimalPathAlg

Finds a solution to a N-Queens problem using either Uniform-Cost search or A* search.

The indexes of the list will represent columns on a chessboard while the numbers in each column will represent the row of the queen location in that column. 

## The Two Algorithms

### A*

The A* algorithm uses a combination of heuristic values and the path cost in order to find the optimal solution. This algorithm is significantly faster than Uniform-Cost.

f(n) = g(n) + h(n) where:
g(n) = path cost
h(n) = heuristic (estimated cost to the goal)

### Uniform-Cost

The Uniform-Cost algorithm uses the path cost in order to find the optimal solution.

f(n) = g(n) where:
g(n) = path cost

## Example

Here is a solution for the 8-Queens problem using the two algorithms

![](https://i.gyazo.com/49f476cd5a6d92b654daf419dfd1303f.png)


## Built With

* Python

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
