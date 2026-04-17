class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head.next)
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        if not curr.next:
            self.tail = curr
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res