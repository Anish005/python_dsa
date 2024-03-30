import sys
sys.stdout = open('CP-sheet/output.txt','w')
sys.stdin = open('CP-sheet/input.txt','r')
'''

'''
def solve(s):
    cnt = 0
    s1 = s.count('map')
    s2  = s.count('pie')
    s3 = s.count('mapie')# couldnt think about it
    return s1+s2-s3
    

t = int(input())
for i in range(t):
    n = int(input())
    s = str(input())
    ans = solve(s)
    print(ans)
