w = int(input())
sums = 0
ans = []
for i in range(w):
    if i%2 == 0:
        ans.append(i)
if w == 2:
    print("NO")
elif w//2 == len(ans):
    print("YES")
else:
    print("NO")
    