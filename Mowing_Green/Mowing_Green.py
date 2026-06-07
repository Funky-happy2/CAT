# Read the input.
# Line 1: S, the size of the (square) green.
# Lines 2-5: S numbers each, the mow counts for the top row, left column,
# bottom row and right column respectively.
def get_input():
    size = int(input())
    top = [int(x) for x in input().split()]
    left = [int(x) for x in input().split()]
    bottom = [int(x) for x in input().split()]
    right = [int(x) for x in input().split()]
    return size, top, left, bottom, right


# Determine how many times Matthew crossed the green.
#
# Let r_i be the times row i was mowed and c_j the times column j was mowed.
# A cell (i, j) shows r_i + c_j, and the answer is sum(r) + sum(c).
#
# The top row gives top[j] = r_0 + c_j and the left column gives
# left[i] = r_i + c_0, while the shared top-left corner is top[0] = r_0 + c_0.
# Summing each border:
#     sum(c) = sum(top)  - S * r_0
#     sum(r) = sum(left) - S * c_0
# so the total is sum(top) + sum(left) - S * (r_0 + c_0)
#                = sum(top) + sum(left) - S * top[0].
def crossings(size, top, left):
    return sum(top) + sum(left) - size * top[0]


# Make main
def main():
    size, top, left, bottom, right = get_input()
    print(crossings(size, top, left))


if __name__ == "__main__":
    main()
