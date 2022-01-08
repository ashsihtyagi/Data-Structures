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


def insert_at_mid(head,data,pos):
    count=1
    if pos==0:
        #print('Head')
        return insert_at_head(head,data)
    if pos>=length_of_ll(head):
        #print("Tail")
        return insert_at_tail(head,data)
    temp=head
    while(pos!=1):
        pos-=1
        temp=temp.next
    new_node=node(data)
    new_node.next=temp.next
    temp.next=new_node

    return head

def delete_at_start(head):
    temp=head
    head=head.next
    #del temp
    return head

def delete_at_end():
    temp=head
    count=1
    while(count<length_of_ll(head)-1):
        count+=1
        temp=temp.next
    temp.next=None
    #print(temp.data)
    #del temp

    return


def delete_at_middle(head,pos):
    count=1
    if pos==0:
        #print('Head')
        return delete_at_start(head)
    if pos>=length_of_ll(head):
        #print("Tail")
        return delete_at_end()
    temp=head
    while(count<pos):
        count+=1
        temp=temp.next
    temp.next=temp.next.next
    return

def find_mid_node(head):
    if head==None:
        return None
    slow=head
    fast=head.next

    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
    #print(fast.data)

    return slow.data


def sum_LL_same_size(head1,head2):
    if head1==None and head2==None:
        return (None,0)

    result=node(0)
    returned_node,carry=sum_LL_same_size(head1.next,head2.next)
    result.next=returned_node
    sum_=head1.data+head2.data+carry
    carry=sum_//10
    result.data=sum_%10
    return(result,carry)

def sum_LL(head1,head2):
    result,carry=sum_LL_same_size(head1,head2)
    if carry==0:
        return result
    n=node(carry)
    n.next=result
    return n


n=int(input())
m=int(input())
#head=None
head1=None
head2=None

#while n>0:
   # n-=1
   # x=int(input())
    #head=insert_at_tail(head,x)

while n>0:
    n-=1
    x=int(input())
    head1=insert_at_tail(head1,x)

while m>0:
    m-=1
    x=int(input())
    head2=insert_at_tail(head2,x)


display_all(head1)
print("\n")

display_all(head2)
print("\n")

sum_=sum_LL(head1,head2)
display_all(sum_)
#print("\n")
#head=insert_at_mid(head,67,0)
#display_all(head)

#mid_node=find_mid_node(head)
#print("Mid_Node=",mid_node)

#print("\n")

#head=insert_at_mid(head,67,2)

#display_all(head)
#print("\n")

#mid_node=find_mid_node(head)
#print("Mid_Node=",mid_node)

#head=delete_at_start(head)
#display_all(head)
#print("\n")

#delete_at_end()
#display_all(head)
#print("\n")

#delete_at_middle(head,1)
#display_all(head)