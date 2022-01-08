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


def reverse_ll(head,k):
    prev=None
    curr=head
    while k>0:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
        k-=1
    return prev


def reverse_group_k(head,k):
    ptr=head
    new_head=None
    last_tail=None
    while ptr!=None:
        count=0
        ptr=head
        while count<k and ptr!=None:
            ptr=ptr.next
            count+=1

        if count==k:
            reverse_head=reverse_ll(head,k)
            if new_head==None:
                new_head=reverse_head

            if last_tail!=None:
                last_tail.next=reverse_head

            last_tail=head
            head=ptr
    if last_tail:
        last_tail.next=head

    return new_head if new_head else head




n = int(input())

    # head=None
head1 = None


while n > 0:
    n -= 1
    x = int(input())
    head1 = insert_at_tail(head1, x)


display_all(head1)
print("\n")




head1=reverse_group_k(head1,3)

display_all(head1)