
from z3 import *

s = Solver()


grid = [[Int('({},{})'.format(i, j)) for j in range(9)] for i in range(9)]

for i in range(9):
    for j in range(9):
        # every grid number must be in [1:9]
        s.add(And(grid[i][j] >= 1, grid[i][j] <= 9))

# given values


# constraints

for i in range(9):
  # every number in a row must be unique and in [1:9]
    s.add(Distinct(grid[i]))
    # s.add(Distinct([grid[i][j] for j in range(9)]))

for j in range(9):
    # every number in a column must be unique and in [1:9]
    s.add(Distinct([grid[i][j] for i in range(9)]))

# every number in the 3x3 squares must be unique
s.add([Distinct([grid[3*i0+i][3*j0+j] for i in range(3) for j in range(3)])
       for i0 in range(3) for j0 in range(3)])

instance = ((0, 0, 0, 0, 9, 4, 0, 3, 0),
            (0, 0, 0, 5, 1, 0, 0, 0, 7),
            (0, 8, 9, 0, 0, 0, 0, 4, 0),
            (0, 0, 0, 0, 0, 0, 2, 0, 8),
            (0, 6, 0, 2, 0, 1, 0, 5, 0),
            (1, 0, 2, 0, 0, 0, 0, 0, 0),
            (0, 7, 0, 0, 0, 0, 5, 2, 0),
            (9, 0, 0, 0, 6, 5, 0, 0, 0),
            (0, 4, 0, 9, 7, 0, 0, 0, 0))

instance_c = [If(instance[i][j] == 0,
                 True,
                 grid[i][j] == instance[i][j])
              for i in range(9) for j in range(9)]

s.add(instance_c)

# print(s.check())
# print(s.model())
if s.check() == sat:
    m = s.model()
    r = [[m.evaluate(grid[i][j]) for j in range(9)]
         for i in range(9)]
    print_matrix(r)
else:
    print("failed to solve")
