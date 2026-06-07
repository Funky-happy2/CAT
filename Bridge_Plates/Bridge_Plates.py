# Read the input.
# Line 1: B, the number of items in the middle layer (always odd).
# Line 2: B numbers. Items at positions 1, 3, 5, ... (1-based) are bricks; the
# value is the stud width. Items at positions 2, 4, ... are gaps, the value
# being the stud width of the base showing through the gap.
def get_input():
    int(input())  # B is implied by the length of the next line.
    layout = [int(x) for x in input().split()]
    return layout


# Build a per-stud list where True means the stud sits on a brick in the
# middle layer and False means it is over a gap. Bricks are the even-indexed
# items (0, 2, 4, ...) of the layout, gaps the odd-indexed ones.
def brick_studs(layout):
    studs = []
    for index, width in enumerate(layout):
        is_brick = (index % 2 == 0)
        studs.extend([is_brick] * width)
    return studs


# Count the ways to fully cover the top layer.
#
# A plate covering studs [i, i + k - 1] is allowed only when both of its end
# studs sit on a brick. We tile the whole width with plates of size 1, 2, 3,
# 4 or 6 laid end to end.
#
# dp[i] = number of ways to cover studs [i, L), assuming a plate starts at i.
# A plate of length k is valid when stud i and stud i + k - 1 are both bricks,
# and it leads to dp[i + k]. dp[L] = 1 (everything covered).
def count_ways(studs):
    plate_sizes = (1, 2, 3, 4, 6)
    length = len(studs)

    dp = [0] * (length + 1)
    dp[length] = 1

    for i in range(length - 1, -1, -1):
        # A plate can only start on a brick stud.
        if not studs[i]:
            continue
        ways = 0
        for k in plate_sizes:
            end = i + k - 1
            if end < length and studs[end]:
                ways += dp[i + k]
        dp[i] = ways

    return dp[0]


# Make main
def main():
    layout = get_input()
    studs = brick_studs(layout)
    print(count_ways(studs))


if __name__ == "__main__":
    main()
