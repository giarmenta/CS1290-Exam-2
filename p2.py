import sys

def path(sq):
    n = len(sq)
    for i in range(n - 2, -1, -1):
        for j in range(n):
            path = sq[i + 1][j]
            if j > 0:
                path = min(path, sq[i + 1][j - 1])
            if j + 1 < n:
                path = min(path, sq[i + 1][j + 1])
            sq[i][j] = sq[i][j] + path

    result = sys.maxsize

    for i in range(n):
        result = min(result, sq[0][i])

    return result


square = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(path(square))
