t = int(input())
for _ in range(t):
    n, x = map(int,input().split())
    arr = list(map(int, input().split()))
    last = 0
    res =  -1
    for i in range(n):
        res = max(res,arr[i] - last)
        last = arr[i]
    res = max(res,2*(x-last))
    print(res)
        
    
                    