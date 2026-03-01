n=int(input())
arr=list(map(int,input().split()))
s=int(input())
sorted=[]
while s>0 and arr:
    move=arr.index(max(arr))
    if s>=move:
        sorted.append(max(arr))
        s-=move
        del arr[move]
    else:
        move_s=arr.index(max(arr[:s+1]))
        sorted.append(max(arr[:s+1]))
        s-=move_s
        del arr[move_s]

print(' '.join(map(str,sorted+arr)))