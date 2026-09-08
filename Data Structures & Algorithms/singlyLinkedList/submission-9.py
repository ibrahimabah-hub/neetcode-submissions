class LinkedList:
    
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
        def setNext(self, node):
            self.next = node
        def getNext(self):
            return self.next
        def getVal(self):
            return self.val

    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.getVal()
            cur = cur.getNext()
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_head = self.Node(val)
        new_head.setNext(self.head)
        self.head = new_head            

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = self.Node(val)
            return
        cur = self.head
        while cur.getNext():
            cur = cur.getNext()
        cur.setNext(self.Node(val))

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.getNext()
            return True
        
        i = 0
        cur = self.head
        prev = None
        while cur:
            if i == index:
                prev.setNext(cur.getNext())
                return True
            prev = cur
            cur = cur.getNext()
            i += 1
        return False

    def getValues(self) -> List[int]:
        cur = self.head
        values = []
        while cur:
            values.append(cur.getVal())
            cur = cur.getNext()
        return values