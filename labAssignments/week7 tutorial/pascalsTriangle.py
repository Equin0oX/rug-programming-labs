def triangeMaker(rows):
    triangle = [[1]]
    for i in range(2, rows + 1):
        row = [1]
        for j in range(i - 2):
            row.append(triangle[-1][j] + triangle[-1][j + 1])
        row.append(1)
        triangle.append(row)
    return triangle

result = triangeMaker(int(input()))

for line in result:
    print(line)