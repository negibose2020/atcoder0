import bisect

sysin=sys.stdin.readline

N,M,K=map(int,inp().split())
a=list(map(int,inp().split()))
b=list(map(int,inp().split()))

# print(K)
# print(a)
# print(b)
# N,M=3,4
# K=240
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
    bookB=bisect.bisect_right(accum_b,Kb)-1
    if j+bookB>ans:
        ans=j+bookB
    else:
        pass

print(ans)