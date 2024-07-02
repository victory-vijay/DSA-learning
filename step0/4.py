def print_pattern(n):
    size = 2 * n - 1
    pattern = [[0] * size for _ in range(size)]

    for i in range(n):
        for j in range(i, size - i):
            pattern[i][j] = pattern[j][i] = pattern[size -
                                                    i - 1][j] = pattern[j][size - i - 1] = n - i

    for row in pattern:
        print(" ".join(map(str, row)))


# Example usage:
print_pattern(6)
