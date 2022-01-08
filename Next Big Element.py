def nextGreater(li):
    n=len(li)
    result=[-1]*n
    st=[]

    for i in range(2*n):
        while not len(st)==0 and li[st[-1]]<li[i%n]:
            popped=st[-1]
            st.pop()
            result[popped]=li[i%n]

        st.append(i%n)

    return result


li=[int(x) for x in input().split()]

print(nextGreater(li))