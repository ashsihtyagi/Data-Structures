
class stack:
    arr=[]
    top=-1

    def __init__(self,n):
        self.arr=[0]*n

    def push(self,element):
        if self.top>=len(self.arr):
            print("Length: ",len(self.arr))
            print("Over flow")
            return

        self.top += 1
        self.arr[self.top]=element
        return self.top


    def pop(self):
        if self.top<0:
            print("Under flow")
            return

        temp=self.arr[self.top]
        self.top-=1
        return temp


    def peek(self):
        if self.top<0:
            print("Under flow")
            return

        return (self.arr[self.top])

    def stack_length(self):
        if len(self.arr)==0:
            return 0

        return len(self.arr)




def sorted_list(st, element,top):
    if top<0:
        st.push(element)
        return

    if top>=st.stack_length()-1:
        print("len:", top)
        print("Over flow")
        return

    x=st.peek()
    if x<=element:
        top+=1
        st.push(element)
        return

    temp=st.pop()
    top-=1

    sorted_list(st,element,top)
    st.push(temp)
    return

def sort(st,top):
    if top<0:
        return

    temp=st.pop()
    top-=1
    sort(st,top)
    sorted_list(st,temp,top)
    return

n=int(input())
x=int(input())
element=int(input())
top=x+1
st=stack(n)

while(x>0):
    x-=1
    a=st.push(int(input()))


sort(st,a)

#print("A:",a)

sorted_list(st,element,a)

while(top >0):
    top-=1
    print(st.pop())






