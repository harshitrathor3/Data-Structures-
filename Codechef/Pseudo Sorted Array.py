for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(n-1):
        if cnt>1:
            break
        if arr[i+1]<arr[i]:
            cnt+=1
            if i>0:
                if arr[i+1]>=arr[i-1]:
                    arr[i+1], arr[i] = arr[i], arr[i+1]
                else:
                    cnt=2
                    break
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    if cnt>1:
        print('NO')
    else:
        print('YES')
