def count_subarrays(arr,k):
    n=len(arr)
    l,r=0,0
    sum_=0
    res=0
    while r<n:
        sum_ += arr[r]
        while l<=r and sum_>k:
            sum_-=arr[l]
            l+=1
        res+=(r-l+1)
        r+=1
    return res
li=[int(x) for x in input().split()]
k=int(input())
print(count_subarrays(li,k))