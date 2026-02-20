class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        
        # dummy head and tail nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head


    # add node before tail (most recently used)
    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node


    # remove node from linked list
    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


    # get value
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            
            # move to most recent
            self._remove(node)
            self._add(node)
            
            return node.value
        
        return -1


    # insert or update value
    def put(self, key, value):
        
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add(new_node)
        
        # remove least recently used if capacity exceeded
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]



# Testing
cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))  # 10

cache.put(3, 30)     # removes key 2

print(cache.get(2))  # -1

cache.put(4, 40)     # removes key 1

print(cache.get(1))  # -1
print(cache.get(3))  # 30
print(cache.get(4))  # 40