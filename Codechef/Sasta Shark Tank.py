for _ in range(int(input())):
    x1, x2 = map(int, input().split())
    x1 = x1*100/10
    x2 = x2*100/20
    if x1>x2:
        print('FIRST')
    elif x2>x1:
        print('SECOND')
    else:
        print('ANY')
