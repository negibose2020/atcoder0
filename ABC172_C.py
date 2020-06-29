import numpy as np

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

accum_a=np.cumsum(a)
accum_a=accum_a[accum_a <K]
accum_a=np.append(accum_a,K)
accum_a=np.insert(accum_a,0,0)

accum_b=np.cumsum(b)

ans=0
# print(accum_a)
# print(accum_b)
# print(len(accum_a))


for j in range (len(accum_a)-1):
    Kb=K-accum_a[j]
    _accum_b=accum_b
    _accum_b=np.append(_accum_b,Kb)
    _accum_b1=np.sort(_accum_b)
    bookb=np.where(_accum_b1==Kb)
    bookb=np.amax(bookb)

    if j+bookb>ans:
        ans=j+bookb
    else:
        pass

print(ans)