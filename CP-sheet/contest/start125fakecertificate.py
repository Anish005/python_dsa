import sys
sys.stdout = open('CP-sheet/output.txt','w')
sys.stdin = open('CP-sheet/input.txt','r')

def max_zero_sequence(arr):
    window = 0
    max_window = 0
    for bit in arr:
        if bit == '0':
            window += 1
        else:
            window = 0
        max_window = max(window, max_window)
    return max_window

def count_one(arr):
    return arr.count('1')

def solve(s,n):
    return max_zero_sequence(s) + count_one(s)

t = int(input())
for i in range(t):
    n = int(input())
    s = str(input())
    ans = solve(s,n)
    print(ans)    