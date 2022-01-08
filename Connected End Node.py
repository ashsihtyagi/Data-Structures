class node:
    data=-1
    next=None

    def __init__(self,data):
        self.data=data

def length_of_ll(head):
    count=0
    temp=head
    while(temp!=None):
        count+=1
        temp=temp.next
    #print(count)
    return count

def display_all(head):
    temp=head
    while (temp!=None):
        print(temp.data,end="->")
        temp=temp.next

    return


def insert_at_head(head,data):
    if head==None:
        return node(data)

    new_node=node(data)
    new_node.next=head
    head=new_node
    #print (head.data)
    return head

def insert_at_tail(head,data):
    if head==None:
        return node(data)

    temp=head
    while temp.next!=None:
        temp=temp.next

    new_node=node(data)
    temp.next=new_node

    return head

def end_of_ll(head,x):
    temp=head

    while(temp.next!=None):
        x-=1
        temp=temp.next
        if x==0:
            temp2=temp
    temp.next=temp2
    temp2.next=None
   # return (head,x)

def find_the_loop_node(head):
    slow=head
    fast=head.next
    new=head

    while(fast!=None and fast.next!=None and fast!=slow):
        slow=slow.next
        fast=fast.next.next

    while(slow!=new):
        slow=slow.next
        new=new.next
    print(slow.data)
    return slow.data

n=int(input())
x=int(input())
head=None
while(n>0):
    n-=1
    data=int(input())
    head=insert_at_tail(head,data)


display_all(head)

end_of_ll(head,x)

print(find_the_loop_node(head))
#display_all(head)