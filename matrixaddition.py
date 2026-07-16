# Matrix A
A = [
    [1, 2],
    [3, 4]
]

# Matrix B
B = [
    [5, 6],
    [7, 8]
]

# Result matrix
result = [
    [0, 0],
    [0, 0]
]

# Matrix addition
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

# Printing result
for row in result:
    print(row)