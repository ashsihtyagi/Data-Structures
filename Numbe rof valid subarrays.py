def subarrays(li):
    st=[]
    n=len(li)
    ans=0
    for i in range(n):
        while not len(st)==0 and li[st[-1]]>li[i]:
            st.pop()

        st.append(i)
        ans+=len(st)

    return ans


li=[int(x) for x in input().split()]

print(subarrays(li))