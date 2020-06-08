import math

A,B,X=map(int,input().split())

if X<A+B:
    print(0)
    exit()
if X>=10**9*A+9*B:
    print(10**9)
    exit()

min=0
max=10**9+1
N=(min+max)//2
D=int(math.log10(N)+1)

if A*N+B*D<X
    N=N/2
else:
    N=N+N/2








N=1
arr2=sorted(arr)
N_from=arr2[arr2.index(X)-1]
if arr2[-1]==X:
    N_to=X
else:
    N_to=arr2[arr2.index(X)+1]
Ns=sorted([N_from,N_to])

N=Ns[0]
print(N)
print(A*N+B*D1>X)

if A*N+B*D1>X:
    flg=A*N+B*D1>X
    D2=int(math.log10(N-1)+1)
    while flg==True:
        N-=1
else:
    flg==A*N+B*D1<=X
    D2=int(math.log10(N+1)+1)
    while flg==True:
        N+=1

print(N)