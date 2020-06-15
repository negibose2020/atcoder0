X,N=map(int,input().split())
if N==0:
    print(X)
    exit()

P_ori=list(map(int,input().split()))
if P_ori.count(X)==0:
    print(X)
    exit()


P1=sorted(P_ori)
N=list(range(0,102))
PZ=[]
for i in range(len(N)):
    if P1.count(N[i])==0:
        PZ.append(N[i])

PZ.append(X)
P2=sorted(PZ)
t=P2.index(X)
if P2[t]==P2[0]:
    print(P2[1])
    exit()
elif P2[t]==P2[-1]:
    print(P2[-2])
    exit()
else:
    dist1=abs(P2[t-1]-P2[t])
    dist2=abs(P2[t]-P2[t+1])
    if dist1<=dist2:
        print(P2[t-1])
        exit()
    else:
        print(P2[t+1])
        exit()
print(0)