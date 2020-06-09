N,K=map(int,input().split())
# S=list(map(int,input().split()))
_=input().split()
S=[]
for s in _:
    S.append((int(s)+1)/2) #初めから期待値で配列作成

# K=4
# S=[17, 13, 13, 12, 15, 20, 10, 13, 17, 11]
# K=3
# S=[1,2,2,4,5]

maxsum=0

for i in range(len(S)):  #ここがrange(len(S)-K)ではダメっぽいのがわからない・・・
    tempsum=sum(S[i:i+K])
    if maxsum<tempsum:
        maxsum=tempsum
    else:
        pass

print(maxsum)