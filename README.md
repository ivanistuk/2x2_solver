# 2x2_solver
Solver for a 2x2 Rubik's Cube using the Breadth First Search algorithm.
The solver uses two Breadth First Search algorithms, one starting from the solved cube and one starting from the cube it is solving. When one algorithm finds a cube that is present in the visited cubes of the other algorithm, it has found a solution.

# Usage
The input of the program is a string of 24 numbers where each number represent a color:

    1: white
    2: orange
    3: green
    4: red
    5: blue
    6: yellow

in the following pattern:

          0  1
          2  3
    4  5  8  9 12 13 16 17
    6  7 10 11 14 15 18 19
         20 21
         22 23
      
For example a solved cube would be represented by the number:

    111122223333444455556666
      
The output is a string of moves in standard Rubik's notation.

Pypy is recommended for a much faster average solving time, especially for longer solutions.
