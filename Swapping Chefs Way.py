for _ in range(int(input())):
    n = int(input())
    s = list(input())
    t=list(s)
    for i in range(n//2):
        if s[i]>s[n-i-1]:
            s[i], s[n-i-1] = s[n-i-1], s[i]
    if sorted(t)==s:
        print('Yes')
    else:
        print('No')
