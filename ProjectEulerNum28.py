#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
import math

limit = 1001 * 1001 + 1
answer = 0

bottom_right = [3]

for k in range(0, 1000):
    if (8*k + 10 + bottom_right[-1]) < limit:
        bottom_right.append(8*k + 10 + bottom_right[-1])
    else:
        break

bottom_left = [5]

for k in range(0, 1000):
    if (8*k + 10 + bottom_left[-1]) < limit:
        bottom_left.append(8*k + 12 + bottom_left[-1])
    else:
        break

top_left = [7]

for k in range(0, 1000):
    if (8*k + 10 + top_left[-1]) < limit:
        top_left.append(8*k + 14 + top_left[-1])
    else:
        break

top_right = [k*k for k in range(1,1002,2)]

diagonals = bottom_right + bottom_left + top_left + top_right

for num in diagonals:
    answer += num

print(answer)