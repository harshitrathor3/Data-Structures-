for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    c1 = arr.count(-1)
    c2 = arr.count(1)
    if abs(c1-c2)<=2:
        if abs(c1-c2)==2:
            if c1%2==0:
                print('Yes')
            else:
                print('No')
        else:
            print('Yes')
    else:
        print('NO')
