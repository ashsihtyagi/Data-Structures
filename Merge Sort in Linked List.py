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


def find_mid_node(head):
    if head==None:
        return head
    slow=head
    fast=head.next

    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
    #print(fast.data)

    return slow


def merge_sorted_LL(left,right):
    if left==None:
        return right
    if right==None:
        return left

    result = None
    if left.data<right.data:
        result=left
        result.next=merge_sorted_LL(left.next,right)
    else:
        result =right
        result.next = merge_sorted_LL(left, right.next)

    return result


def mergesort(head):
    if head==None or head.next==None:
        return head

    mid=find_mid_node(head)
    left=head
    right=mid.next
    mid.next = None
    left=mergesort(left)
    right=mergesort(right)
    result=merge_sorted_LL(left,right)
    return result







n=int(input())
head1=None

while n>0:
    n-=1
    x=int(input())
    head1=insert_at_tail(head1,x)

display_all(head1)
print("\n")

#print(find_mid_node(head))

head1=mergesort(head1)
display_all(head1)