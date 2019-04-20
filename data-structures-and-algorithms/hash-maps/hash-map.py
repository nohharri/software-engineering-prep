class HashMap:
    def __init__(self):
        self.storage_size = 16
        self.arr = [None] * self.storage_size
    
    def print_(self):
        print(self.arr)


hash_map = HashMap()
hash_map.print_()