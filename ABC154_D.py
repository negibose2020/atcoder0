N,K=map(int,input().split())
S=list(map(int,input().split()))

# K=4
# S=(17, 13, 13, 12, 15, 20, 10, 13, 17, 11)
# K=3
# S=[1,2,2,4,5]

# K個連続した区間での最大が期待値の最大として、SでK個連続した最大値を探す。
maxSKsum=0
startSindex=0

#1.大きい区間を探す
for i in range(len(S)):  #ここがrange(len(S)-K)ではダメっぽいのがわからない・・・
    tempSKsum=sum(S[i:i+K])
    if maxSKsum<tempSKsum:
        maxSKsum=tempSKsum
        startSindex=i
    else:
        pass

#2.1で探した大きい区間の計算をする。
EV=0
for s in range(K):
    tempEV=S[startSindex+s]*(S[startSindex+s]+1)/2/S[startSindex+s]
    EV+=tempEV

print(EV)