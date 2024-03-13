import sys
sys.stdout = open('CP-sheet/output.txt','w')
sys.stdin = open('CP-sheet/input.txt','r')

def solve(a,n):
    for i in range(1,n-1):
        if a[i-1] <= a[i+1] and a[i] >= 2*a[i-1]:
            a[i+1] -= a[i-1]
            a[i] -= 2*a[i-1]
            a[i-1] = 0
    zero  = True
    for i in range(n):
        if a[i] != 0:
            zero = False
            break
    if zero:
        return 'YES'
    else:
        return 'NO'
    return



t = int(input())
for i in range(t):
    n = int(input())
    a =  list(map(int,input().split()))
    ans = solve(a,n)
    print(ans)
        
    
