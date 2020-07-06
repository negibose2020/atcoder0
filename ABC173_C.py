import numpy as np

H,W,K=map(int,input().split())
E=[]
for e in range(H):
    _=input()
    temp=_.replace('#','1').replace('.','0')
    
    E.append(list(map(int,temp)))

Arr=np.array(E)
# print(Arr)
FA=0

for h in range (2**H):
    # print("h:{0}が始まるよ。".format(h))
    select_H=[]
    for i in range (H):
        if (h>>i) & 1==1:
            select_H.append(1)
        else:
            select_H.append(0)
    sHarr=np.array(select_H)
    delSHarr=np.where(sHarr==1)
    # print(sHarr)
    # print(delSHarr)
    _ans=np.delete(Arr,delSHarr,axis=0)
    # print('________________ans__________________')
    # print(_ans)

    for w in range (2**W):
        # print("w:{0}が始まるよ。".format(w))
        select_W=[]
        for j in range (W):
            if (w>>j) &1 ==1:
                select_W.append(1)
            else:
                select_W.append(0)
        sWarr=np.array(select_W)
        delsWarr=np.where(sWarr==1)
        ans=np.delete(_ans,delsWarr,axis=1)
        # print("***ans***")
        # print(ans)

        if np.sum(ans)==K:
            FA+=1

print(FA)



# for x in range(2**H):
    
    # ans=np.delete(_ans,sWarr,axis=1)
# print(ans)
