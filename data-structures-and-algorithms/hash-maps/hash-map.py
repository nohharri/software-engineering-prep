class Node():
    def __init__(self):
        self.key = None
        self.val = None


class HashMap:
    def __init__(self):
        self.size = 0
        self.storage_size = 20
        self.arr = [None] * self.storage_size

    # if hash map cannot find the value, then insert it
    # this get only supports numbers
    def get(key):
        return self.arr[self._hash(key)]
        
    def set(key, val):
        if self.size < self.storage_size:
            idx = self._hash(key)
            return idx
        
    # returns the index within the array
    # hash function is key mod storage size (x mod k)
    def _hash(key):
        idx = key % self.storage_size
        while self.arr[idx] and self.arr[idx].key != key and idx < self.storage:
            idx = idx + 1
        return idx

hash_map = HashMap()
hash_map.print_()