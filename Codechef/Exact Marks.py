from math import ceil
for _ in range(int(input())):
    n, x = map(int, input().split())
    if x>n*3:
        print('No')
        continue
    i = ceil(x/3)
    if i==n+1:
        print('No')
    if i*3==x:
        print('Yes')
        print(i, 0, n-i)
    else:
        sub = (i*3)-x
        if sub<=n-i:
            print('Yes')
            print(i, sub, n-i-sub)
        else:
            print('No')
