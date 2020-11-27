class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i range(self.size)]
        self.count = 0

    # hashing function using remainder to reduce collisions
    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size
    
    # function to add elements to the hashtable
    def put(self, key, value):
        item = HashTable(key, value)
        h = self._hash(key)

        while self.slots[h].key is key:
            if self.slots[h] is key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
    
    # function to return values given a certain key
    def get(self, key):
        h = self._hash(key)
        while self.slots[h] is None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h + 1) % self.size
        return None
