for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if n==1:
        print(arr[0])
        continue
    for i in range(n):
        arr[i] = abs(arr[i])
    ans1 = sum(arr[::2])-sum(arr[1::2])
    minval=10000000000
    maxval=-10000000000
    mx=arr[1]
    mn=arr[0]
    for i in range(0, n-1, 2):
        if arr[i]<minval:
            mn=i
            minval = arr[i]
        if arr[i+1]>maxval:
            mx=i+1
            maxval=arr[i+1]
    if n%2==1:
        if arr[n-1]<minval:
            mn=n-1
            minval=arr[n-1]
    arr[mx], arr[mn] = arr[mn], arr[mx]
    ans2=sum(arr[::2])-sum(arr[1::2])
    if ans1>ans2:
        print(ans1)
    else:
        print(ans2)
