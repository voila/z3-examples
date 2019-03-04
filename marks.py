from z3 import *

people = ["Alan", "Barbara", "Charles", "David", "Ellen"]

marks = {}
for p in people:
    marks[p] = [Int("{}_{}".format(p, i)) for i in range(5)]

s = Solver()

# 1 <= marks <= 5
for p in people:
    for m in marks[p]:
        s.add(And(m >= 1, m <= 5))

# Allan marks add up to 24
s.add(sum(marks["Alan"]) == 24)

# Ellen got 5 in Maths (3), and 3 in Sciences (4)
s.add(marks["Ellen"][3] == 5)
s.add(marks["Ellen"][4] == 3)

# Charles has 4 identical marks
s.add(Or(
    And(marks["Charles"][0] == marks["Charles"][1],
        marks["Charles"][1] == marks["Charles"][2],
        marks["Charles"][2] == marks["Charles"][3]),

    And(marks["Charles"][0] == marks["Charles"][1],
        marks["Charles"][1] == marks["Charles"][2],
        marks["Charles"][2] == marks["Charles"][4]),

    And(marks["Charles"][0] == marks["Charles"][1],
        marks["Charles"][1] == marks["Charles"][3],
        marks["Charles"][3] == marks["Charles"][4]),

    And(marks["Charles"][0] == marks["Charles"][2],
        marks["Charles"][2] == marks["Charles"][3],
        marks["Charles"][3] == marks["Charles"][4]),

    And(marks["Charles"][1] == marks["Charles"][2],
        marks["Charles"][2] == marks["Charles"][3],
        marks["Charles"][3] == marks["Charles"][4])
))
# rankings of sum of all marks: Alan > Barbara > Charles > David > Ellen
s.add(And(sum(marks["Alan"]) > sum(marks["Barbara"]),
          sum(marks["Barbara"]) > sum(marks["Charles"]),
          sum(marks["Charles"]) > sum(marks["David"]),
          sum(marks["David"]) > sum(marks["Ellen"])))

# in each subject, everybody must have different marks
for i in range(5):
    s.add(Distinct(marks["Alan"][i],
                   marks["Barbara"][i],
                   marks["Charles"][i],
                   marks["David"][i],
                   marks["Ellen"][i]))


print(s.check())
print(s.model())
