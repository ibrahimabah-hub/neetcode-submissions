class MyLinkedList:

    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = None

    def get(self, index: int) -> int:
        cur = self.head
        while cur:
            if index==0:
                return cur.val
            index-=1
            cur=cur.next
        return -1

    def addAtHead(self, val: int) -> None:
        newhead = self.Node(val)
        newhead.next = self.head
        self.head = newhead

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = self.Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.Node()
        tmp = self.Node(val)
        if index == 0:
            cur = tmp
            cur.next = self.head
            self.head = cur
            return
        
        cur.next = self.head    
        while cur:
            if index == 0:
                tmp.next = cur.next
                cur.next = tmp
                return
            index-=1
            print(f"{cur.val}->")
            cur = cur.next
            
        cur = None


    def deleteAtIndex(self, index: int) -> None:
        cur = self.Node()
        cur.next=self.head
        if index == 0:
            self.head = self.head.next
            return

        while cur.next:
            if index==0:
                cur.next=cur.next.next
                return
            index-=1
            cur = cur.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)