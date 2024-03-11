#链表：
#头插法
list1 =[1,2,3,4,5]
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

def create_linklist_head(li): 
    head = Node(li[0]) #create headnode(iniailize linklist)
    for element in li[1:]:
        node = Node(element) 
        node.next = head #更新next
        head = node #更新item
    return head
lk1 = create_linklist_head(list1)

def create_linklist_tail(li):
    head = Node(li[0]) # iniailize linklist
    node = head 
    for element in li[1:]: 
        tail = Node(element)
        node.next = tail
        node = node.next
    return head






def print_linklist(lk): #traversal linklist
    while lk:
        print(lk.item, end=',')
        lk = lk.next


lk2 = create_linklist_tail(list1)
print_linklist(lk1)
print_linklist(lk2)