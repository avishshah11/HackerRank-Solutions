x = int(input())
y = map(int, input().split())
z = tuple(y)
print(hash(z))