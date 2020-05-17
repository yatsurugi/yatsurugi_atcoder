n, x, y = map(int, input().split())
x, y = x-1, y-1

# ループさせて最短距離nに該当するものが見つかるたびに、その添字の箇所を１ずつ増やしていく
ans = [0] * n
for i in range(n):
    for j in range(i+1, n):
        ind = min(j-i, abs(x-i)+abs(y-j)+1) # 模範回答には、abs(y-i)+abs(x-j)+1が必要と書いてあるが、なくてもAC
        ans[ind] += 1                       # i<j、x<yと大小関係が確定しているため。iとjを全検索していたら必要。

for k in range(1, n):
    print(ans[k])
