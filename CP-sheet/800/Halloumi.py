import sys
sys.stdout = open('CP-sheet/output.txt','w')
sys.stdin = open('CP-sheet/input.txt','r')



t = int(input())
for i in range(t):
    n, k =  map(int,input().split())
    arr =  list(map(int,input().split()))
    if k == 1 and arr != sorted(arr):
        print('NO')
    else:
        print('YES')

