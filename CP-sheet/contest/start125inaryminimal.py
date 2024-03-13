import sys
sys.stdout = open('CP-sheet/output.txt','w')
sys.stdin = open('CP-sheet/input.txt','r')



def solve(s):
    pass


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = str(input())
    ans = solve(s,n)
    print(ans)