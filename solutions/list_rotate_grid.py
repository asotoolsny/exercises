# Rotate the given grid 90 degrees.
#
# Input: [
#   [".", ".", ".", ".", ".", "."],
#   [".", "0", "0", ".", ".", "."],
#   ["0", "0", "0", "0", ".", "."],
#   ["0", "0", "0", "0", "0", "."],
#   [".", "0", "0", "0", "0", "0"],
#   ["0", "0", "0", "0", "0", "."],
#   ["0", "0", "0", "0", ".", "."],
#   [".", "0", "0", ".", ".", "."],
#   [".", ".", ".", ".", ".", "."],
# ]
#
# Output: [
#     ['.', '.', '0', '0', '.', '0', '0', '.', '.'],
#     ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
#     ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
#     ['.', '.', '0', '0', '0', '0', '0', '.', '.'],
#     ['.', '.', '.', '0', '0', '0', '.', '.', '.'],
#     ['.', '.', '.', '.', '0', '.', '.', '.', '.']
# ]


def rotate_grid(grid):
    rotated = []
    width = len(grid[0])

    for col_index in range(width):
        new_row = []

        for row in grid:
            new_row.append(row[col_index])

        rotated.append(new_row)

    return rotated


def pretty_print(grid):
    for row in grid:
        print("".join(row))


sample_grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "0", "0", ".", ".", "."],
    ["0", "0", "0", "0", ".", "."],
    ["0", "0", "0", "0", "0", "."],
    [".", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "."],
    ["0", "0", "0", "0", ".", "."],
    [".", "0", "0", ".", ".", "."],
    [".", ".", ".", ".", ".", "."]
]

pretty_print(sample_grid)
print('_'*9)

pretty_print(rotate_grid(sample_grid))
