n = int(input())

print("Matriks A")
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Matriks B")
B = []
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

result = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += A[i][k] * B[k][j]

print("Matriks AXB")
for i in range(n):
    print(' '.join(map(str, result[i])))