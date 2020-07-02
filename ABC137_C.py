from collections import Counter

N=int(input())
l=[]
v=[]

ans=0

for i in range(N):
    si=input()
    # ci=Counter(si)
    # c=sorted(ci.elements())
    # c=sorted(Counter(si).elements())
    sorted_s=''.join(sorted(Counter(si).elements()))
    if sorted_s in l:
        ans+=v[l.index(sorted_s)]
        v[l.index(sorted_s)]+=1
    else:
        l.append(sorted_s)
        v.append(1)

print(ans)