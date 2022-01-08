class stack:
    arr=[]
    top=-1

    def __init__(self,n):
        self.arr=[-1]*n

    def push(self,element):
        if self.top>=len(self.arr):
            self.isfull()
            return

        self.top+=1
        self.arr[self.top]=element
        print("Top",self.top)
        return self.top



    def pop(self):
        if self.top<0:
            self.isempty()
        else:
            self.arr[self.top]=-1
            self.top-=1
        return self.top

    def isempty(self):
        print("Stack is empty")
        return

    def isfull(self):
        print("Stack is full")
        return


    def display(self):
        x=self.top
        while x>-1:
            print(self.arr[x],end=" ")
            x-=1
        print(" ")
        return 

def rectangle(l):
    
    s=stack(5)
    top=-1
    a=0
    ans=9999999
    for i in range(0,):
        if top==-1:
            top+=1
            s.push(l[i])

        if l[i]>s[top]:
            top+=1
            s.push(i)
        if l[i]<s[top]:
            while(l[i]>s[top]):
                a=s.pop()
                top-=1
                if top==0 and ans>(a-s[top])*l[a]:
                    ans=(l[a]-s[top])*l[a]


def len(self,s):
    len=self.top+1
    return len




s=stack(7)
a=s.push(2)
a=s.push(8)
a=s.push(10)
a=s.push(9)
a=s.push(22)

s.display()

a=s.pop()
a=s.pop()
s.display()
print(s.len(s))
ans=rectangle(s)
print(ans)