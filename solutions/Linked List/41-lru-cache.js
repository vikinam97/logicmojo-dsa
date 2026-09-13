class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
    
    def toString(self):
        return f"({self.key}, {self.value})"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def add_first(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            self.len += 1
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

        self.len += 1
    
    def remove_last(self):
        if self.len == 0:
            return

        delNode = self.tail
        if self.head == delNode:
            self.head = None
            self.tail = None
            self.len -= 1
            return delNode

        self.tail = delNode.prev
        self.tail.next = None
        delNode.prev = None
        self.len -= 1

        return delNode

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        node.next = None
        node.prev = None

        self.len -= 1

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = {}
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        
        node = self.key_node[key]
        self._update(node.key, node.value)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            return self._update(key, value)
        
        if self.list.len == self.capacity:
            self._evict()
        
        self._add_new(key, value)
    
    def _add_new(self, key, value):
        node = Node(key, value)
        self.list.add_first(node)
        self.key_node[key] = node
        return node

    def _update(self, key, value):
        node = self.key_node[key]
        node.value = value
        self.list.remove(node)
        self.list.add_first(node)
    
    def _evict(self):
        node = self.list.remove_last()
        if  not node:
            return 
        del self.key_node[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)