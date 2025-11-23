r, c = map(int, input().split())
elements = list(map(int, input().split()))
for i in range(r):
    row = elements[i * c : (i + 1) * c]
    print(' '.join(map(str, row)))