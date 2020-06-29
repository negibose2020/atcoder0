N,M,K=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

# print(K)
# print(a)
# print(b)
# N,M=3,4
# K=730
# a=[60, 90, 120]
# b=[80, 150, 80, 150]

ans=0

accum_a=[0]
for i in a:
    _a=accum_a[-1]+i
    if _a>K:
        break
    else:
        accum_a.append(_a)
accum_a.append(K)

accum_b=[0]
for i in b:
    accum_b.append(accum_b[-1]+i)

ans=0

for j in range (len(accum_a)-1):
    Kb=K-accum_a[j]
    _accum_b=accum_b
    _accum_b.append(Kb)
    _accum_b1=sorted(_accum_b)
    bookb=_accum_b1.index(Kb)-1
    if _accum_b.count(Kb)==2:
        bookb+=1
    if j+bookb>ans:
        ans=j+bookb
    else:
        continue
print(ans)
