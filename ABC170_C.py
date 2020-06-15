X, N = map(int,input().split())
if N == 0:
    print(X)
    exit()

p = list(map(int,input().split()))
if p.count(X) == 0:
    print(X)
    exit()


l = list(range(0,102)) #ここの範囲設定が一番難しい部分だと思う
flist = []
for i in range(len(l)):
    if p.count(l[i]) == 0:
        flist.append(l[i])


flist.append(X)
anslist = sorted(flist)
t = anslist.index(X)

dist1 = anslist[t] - anslist[t-1] #Xと1つ前の数字との距離
dist2 = anslist[t+1] - anslist[t] #Xと1つ後ろの数字との距離
if dist1 <= dist2:
    print(anslist[t-1])
else:
    print(anslist[t+1])