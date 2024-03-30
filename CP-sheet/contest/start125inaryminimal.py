import sys
sys.stdout = open('CP-sheet/output.txt','w')
sys.stdin = open('CP-sheet/input.txt','r')

'''
LOGIC BUILDING CLASS WITH SUBRAT

if  k < no of ones in the string:
    fliping k ones into 0 from left
else
    k >= no of ones in the string:
        delete all ones from left
        then del the rest of zeroes
output ==> smallest lexico string
'''

def count_ones(string):
    return string.count('1')

def solve(s,k):
    n_ones = count_ones(s)
    if n_ones > k:
        s = s.replace('1', '0', k)
    else:
        s = s.replace('1', '').replace('0', '', k - n_ones)
    return s


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = str(input())
    ans = solve(s,k)
    print(ans)