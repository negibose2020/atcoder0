
N,K=map(int,input().split())
_=input().split()
S=[]
for s in _:
    S.append(int(s))

# K=4
# S=[17, 13, 13, 12, 15, 20, 10, 13, 17, 11]
# K=3
# S=[1,2,2,4,5]

EVlist=[]

for i in range(len(S)):
    tempEV=(S[i]*(S[i]+1))/2/S[i]
    EVlist.append(tempEV)

maxEVsum=0

for j in range(len(EVlist)):
    tempEVsum=sum(EVlist[j:j+K])
    if maxEVsum<tempEVsum:
        maxEVsum=tempEVsum

print(maxEVsum)