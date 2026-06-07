# Read the input.
# Line 1: the amount of digits.
# Line 2: the digits themselves, separated by spaces.
def get_input():
    # Read the count (not otherwise needed, but consumes line 1).
    int(input())

    # Read the digits as a list of single-character strings. Pulling out the
    # digit characters works whether or not they are separated by spaces.
    number = [c for c in input() if c.isdigit()]
    return number


# Determine the order in which digits are removed.
# At every step, remove the single digit that leaves the largest number.
#
# Removing one digit makes the number largest when you drop the leftmost
# digit that is smaller than the digit to its right; if the digits are
# non-increasing, you drop the last (rightmost) digit instead. Simulating
# that with a stack gives the whole removal order in O(N) total time.
def removal_order(number):
    digits = list(number)
    order = []   # the digits in the order they are removed
    stack = []   # digits kept so far, scanning left to right

    for digit in digits:
        # While the digit on top of the stack is smaller than the new one,
        # that top digit is the next one to be removed (a "rise" follows it).
        while stack and stack[-1] < digit:
            order.append(stack.pop())
        stack.append(digit)

    # Whatever is left is non-increasing, so it is removed from the right end
    # inward: the top of the stack first, down to the bottom.
    while stack:
        order.append(stack.pop())

    return order


# Make main
def main():
    number = get_input()
    order = removal_order(number)

    # Print the removal order, one digit per line.
    for digit in order:
        print(digit, end= "")


if __name__ == "__main__":
    main()
