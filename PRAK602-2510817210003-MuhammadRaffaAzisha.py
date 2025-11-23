n = int(input())
zetsu = list(map(int, input().split()))

result = [str(zetsu[i] * (i + 1)) for i in range(n)]

print(' '.join(result))