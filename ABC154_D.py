# N=20

# EVc=(a*(a+1))/2/a


K=4
S=[17, 13, 13, 12, 15, 20, 10, 13, 17, 11]
max =sum(S[0:K])
startindex=0

for i in range(len(S)-K):
    tempmax=sum(S[i:K])
    if tempmax>max:
        max=tempmax
        startindex=i
    else:
        pass
EVs=[]
for e in range(K):
    tempev=S[startindex+e]*(S[startindex+e]+1)/2/S[startindex+e]
    EVs.append(tempev)
print(sum(EVs))



