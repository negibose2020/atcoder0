def CanIBuy(A,B,mid):
    D=len(str(mid))
    price=A*mid+B*D
    return price


A,B,X=map(int,input().split())

left=0
right=10**9

for i in range(X):

    if CanIBuy(A,B,(left+right)//2)<X:
        _left=left
        _right=right
        '''
        このifの部分は怪しい
        '''
        if left==(_left+_right)//2:
            left+=1
        else:
            left=(_left+_right)//2
    elif CanIBuy(A,B,(left+right)//2)>X:
        _left=left
        _right=right
        '''
        このifの部分は怪しい
        '''
        if right==(_left+_right)//2:
            right-=1
        right=(_left+_right)//2
    else:
        break
    print(i,left,right)

print(left)