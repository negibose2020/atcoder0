from collections import Counter

N=int(input())
L=[]
V=[]

for i in range(N):
    si=input()
    ci=Counter(si)
    c=sorted(ci.elements())
    v=L.count(c)
    if v==0:
        L.append(c)
        V.append(1)
    else:
        ind=L.index(c)
        V[ind]+=1


ans=0

for v in V:
    ans+=v*(v-1)//2

print(ans)