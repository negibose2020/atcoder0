N,K=map(int,input().split())
S=list(map(int,input().split()))

# K=4
# S=(17, 13, 13, 12, 15, 20, 10, 13, 17, 11)
# K=3
# S=[1,2,2,4,5]

maxSKsum=0
startSindex=0

for i in range(len(S)):  #ここがrange(len(S)-K)ではダメないのがわからない・・・
    tempSKsum=sum(S[i:i+K])
    if maxSKsum<tempSKsum:
        maxSKsum=tempSKsum
        startSindex=i
    else:
        pass

EVlist=[]
for s in range(K):
    tempEV=S[startSindex+s]*(S[startSindex+s]+1)/2/S[startSindex+s]
    EVlist.append(tempEV)

print(sum(EVlist))