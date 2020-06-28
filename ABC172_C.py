N,M,K=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

# print(K)
# print(a)
# print(b)
# N,M=3,4
# K=240
# a=[60, 90, 120]
# b=[80, 150, 80, 150]

ans=0
inf=K*2

for i in range (N+M+10):
    if len(a)==1:
        a.append(inf)
    if len(b)==1:
        b.append(inf)
    A=a[0]
    B=b[0]
    if min(A,B)<=K:
        ans+=1
        K-=min(A,B)
        if A<B:
            a.pop(0)
        elif A>B:
            b.pop(0)
        else:
            if A+a[1]<=B+b[1]:
                a.pop(0)
            else:
                b.pop(0)
    else:
        break
print(ans)