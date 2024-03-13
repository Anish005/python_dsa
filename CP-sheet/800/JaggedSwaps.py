import sys
sys.stdout = open('CP-sheet/800/output.txt','w')
sys.stdin = open('CP-sheet/800/input.txt','r')


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0] != 1:
        print('NO')
    else:
        print('YES')
    