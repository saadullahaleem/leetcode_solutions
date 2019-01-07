# https://leetcode.com/problems/lru-cache/

from collections import deque

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = deque([], capacity)
        self.dict = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
            return self.dict[key]
        
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        if len(self.queue) == self.capacity:
            key_to_remove = self.queue.popleft()
            del self.dict[key_to_remove]
        
        if key in self.queue:
            self.queue.remove(key)
            
        self.queue.append(key)    
        self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
