def span(li):
    st=[]
    n=len(li)
    result=[1]*n
    for i in range(n):
        while not len(st)==0 and li[st[-1]]<li[i]:
            st.pop()

        if li[i-1]<li[i] and i!=0:
            result[i]=i-st[-1]
            st.append(i)
        else:
            st.append(i)

    return result

li=[int(x) for x in input().split()]

print(span(li))