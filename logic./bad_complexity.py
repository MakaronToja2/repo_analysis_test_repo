def high_complexity(x, y, z):
    """
    A function designed to have higher cyclomatic complexity.
    It contains multiple if/else branches and a multi-branch (if/elif/else) structure.
    Expected cyclomatic complexity: at least 7 (which typically rates as 'B').
    """
    result = 0

    # Branch 1
    if x > 0:
        result += 1
    else:
        result -= 1

    # Branch 2
    if y > 0:
        result += 2
    else:
        result -= 2

    # Branch 3
    if z > 0:
        result += 3
    else:
        result -= 3

    # Branch 4
    if x + y > z:
        result += 4
    else:
        result -= 4

    # Multi-branch: counts as 2 decisions (if and elif)
    if x > y:
        result *= 2
    elif x == y:
        result += 5
    else:
        result -= 5

    # Branch 6
    if z > 10:
        result /= 2
    else:
        result *= 2

    return result


if __name__ == "__main__":
    # Example invocation
    print("High complexity function output:", high_complexity(5, -3, 10))
