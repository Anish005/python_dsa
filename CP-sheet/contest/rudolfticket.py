import sys
sys.stdout = open('CP-sheet/output.txt','w')
sys.stdin = open('CP-sheet/input.txt','r')

t = int(input())
for i in range(t):
    n, m , k =  map(int,input().split())
    b =  list(map(int,input().split()))
    f =  list(map(int,input().split()))
    cnt = 0
    for i in b:
        for j in f:
            if i + j <= k:
                cnt += 1
    print(cnt)
        
