from z3 import *

# rectangles to fit inside
N = 2
W = [13, 8]
H = [17, 10]

# big rectangle
WM = 20
HM = 30

# variables
x = []
y = []
w = []
h = []

for i in range(N):
    w.append(Int('w{}'.format(i)))
    h.append(Int('h{}'.format(i)))
    x.append(Int('x{}'.format(i)))
    y.append(Int('y{}'.format(i)))


# formula
s = Solver()

for i in range(N):
    # rectangle dimensions
    s.add(w[i] == W[i])
    s.add(h[i] == H[i])

    # all rectangles contained in big rectangle
    s.add(And(x[i] >= 0, x[i] + w[i] <= WM, y[i] >= 0, y[i] + h[i] <= HM))

# rectangles do not overlap
import itertools
for (i,j) in list(itertools.combinations(range(N),N)):    
    s.add(Or(x[i] + w[i] <= x[j], 
             x[j] + w[j] <= x[i],
             y[i] + h[i] <= y[j],
             y[j] + h[j] <= y[i]))
print(s.check())
print(s.model()) 