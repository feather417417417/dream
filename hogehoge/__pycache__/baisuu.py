N, X, Y = map(int, input().split())
for i in range(1, N + 1):
    if i % X != 0 and i % Y != 0:
        print('N')
        continue
    if i % X == 0:
        print('A', end='')
    if i % Y == 0:
        print('B', end='')
    print()