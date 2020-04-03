class Node:
    def __init__(self):
        self.data = 0
        self.next = None

li=[]

class SinglyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size=0

    def insert(self,data):
        node = Node()
        node.data = data
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = node
        self.size+=1

    def DelNode(self,pos):
        cur = self.head
        if pos > self.size:
            return
        for i in range(pos-1):
            cur = cur.next
        cur.next = cur.next.next
        self.size-=1

    def print_list(self):
        cur = self.head.next
        while cur!=None:
            li.append(cur.data)
            cur = cur.next
            
    def reverse(self):
        cur = self.head.next
        while cur.next != None:
            cur = cur.next
        cur.next = Node()
        temp = cur.next
        cur1 = None
        cur2 = self.head.next
        cur3 = cur2.next
        while cur3 != None and cur3.next != None:
            cur2.next = cur1
            cur1 = cur2
            cur2 = cur3
            cur3 = cur3.next
        cur2.next = cur1
        cur3.next = cur2
        self.head = cur3

    def expmul(self,other,length):
        cur = other.head.next
        exp = SinglyLinkedList()
        for i in range(length):
            exp.insert(0)
        for k in range(other.size):
            cur1 = self.head.next
            cur2 = exp.head.next
            for j in range(k):
                cur2 = cur2.next
            for i in range(self.size):
                cur2.data += cur1.data*cur.data
                cur2 = cur2.next
                cur1 = cur1.next
            cur = cur.next
        return exp




exp1 = SinglyLinkedList()
exp2 = SinglyLinkedList()
l = input('Enter the coefficients for 1st expression').split()
for i in range(len(l)-1,-1,-1):
    exp1.insert(int(l[i]))
l = input('Enter the coefficients for 2nd expression').split()
for i in range(len(l)-1,-1,-1):
    exp2.insert(int(l[i]))
n = exp2.size+exp1.size-1
exp = exp2.expmul(exp1,n)
exp.reverse()
exp.print_list()
print(li)