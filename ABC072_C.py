#numpy使用
#arrの条件に合う要素の判定と数の取得

import numpy as np

N=int(input())
a=list(map(int,input().split()))

r=[]

for _ in a:
    l,m,h=_-1,_,_+1
    _r=[l,m,h]
    r.append(_r)
arr=np.array(r)

ans=0
for i in range (max(a)+2):
    _ans=np.sum(np.count_nonzero(arr==i,axis=1))
    if _ans>ans:
        ans=_ans
print(ans)

