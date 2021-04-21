def solve(s):
    ans = [1]
    c = 1
    for i in range(1,len(s)):
        if(s[i] <= s[i-1]):
            c=1
        else:
            c += 1
        ans.append(c)
        
    print(*ans)

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    print(f"Case #%i: "%(1+i),end=" ")
    solve(s)
