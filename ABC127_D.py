

N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
for i in range(M):
    B,C=map(int,input().split())
    for j in range (B):
        if A[j]<C:
            A[j]=C
        else:
            break
    A.sort()

print(sum(A))