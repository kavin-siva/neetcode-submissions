class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Map key to Node
        
        # Dummy nodes for boundaries
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper: Insert node at the rightmost position (Most Recently Used)
    def _insert(self, node: Node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    # Helper: Remove an existing node from the linked list
    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)  # Move to the end (MRU)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)
        
        # Evict Least Recently Used (LRU) node if capacity exceeded
        if len(self.cache) > self.cap:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

        
