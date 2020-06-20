import numpy as np

N=int(input())
A=np.array(list(map(int,input().split())))
'''
以下、方針
・Aから、各要素の出現回数を取得する。
・出現回数から、組み合わせを計算する。
'''
uni,cou=np.unique(A,return_counts=True)
# print(uni)
# print(cou)
com=[]
for i in range(len(cou)):
    c=(cou[i]*(cou[i]-1))//2
    com.append(c)
# com=np.array(com)
# print(com)
totalcombination=sum(com)

'''
以下方針
・Aから数字を取得
・その数字に対応する組み合わせを減らす。
・その数字の出現回数を1減らした状態の組み合わせの数を足す。
'''
for j in range (N):
    n=A[j] #nはAの数列の数字
    f=np.where(uni==n)[0][0]
    t=com[f]
    e=(cou[f]-1)*(cou[f]-2)//2
    print(totalcombination-t+e)