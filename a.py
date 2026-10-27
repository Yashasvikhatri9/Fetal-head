n,m = map(int,input().split())
ans = []
for i in range(n):
    a = []
    if i < n-1:
        a = (["#"]*i)+a
        a+= (["."]*2)
        k = m-2+i
        a+=(["#"]*k)+a
    else:
        a = (["#"]*i)+a
        a+= (["."])
    ans.append(a)
print(ans)