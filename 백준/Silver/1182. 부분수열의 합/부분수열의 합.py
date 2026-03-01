n,s=map(int,input().split())
arr=list(map(int,input().split()))
answer=0
def solve(idx,sum):
    global answer
    if idx>=n:
        return
    sum+=arr[idx]
    if sum==s:
        answer+=1
    solve(idx+1,sum)
    solve(idx+1,sum-arr[idx])
solve(0,0)
print(answer)