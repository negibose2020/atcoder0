import math

A,B,X=map(int,input().split())


N=0
arr=[X,10**9]

if X<A+B:
    print(N)
    exit()
if X>=10**9*A+9*B:
    print(10**9)
    exit()

if A>=B:
    for i in range(1,10):
        _=int((X-i*B)/A)
        arr.append(_)
else:
    for i in range(1,10):
        _=int((X/i)/A)
        arr.append(_)

N=1
arr2=sorted(arr)
N_from=arr2[arr2.index(X)-1]
if arr2[-1]==X:
    N_to=X
else:
    N_to=arr2[arr2.index(X)+1]
Ns=sorted([N_from,N_to])

N=Ns[0]
D=int(math.log10(N)+1)


while A*N+B*D<=X:
    N+=1
print(N)