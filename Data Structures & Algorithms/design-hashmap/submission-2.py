class MapItem:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap:
    def __init__(self):
        self.map = [[]] * 4
        self.next_size = len(self.map) * 2

    def put(self, key: int, value: int) -> None:
        self.__ensure_resized()
        self.__add_or_update_item(key, value)

    def get(self, key: int) -> int:
        bucket = self.map[self.__get_hash(key)]

        for entry in bucket:
            if entry.key == key:
                return entry.val 
        
        return -1

    def remove(self, key: int) -> None:
        bucket = self.map[self.__get_hash(key)]
        self.map[self.__get_hash(key)] = [entry for entry in bucket if entry.key != key]
    
    def __add_or_update_item(self, key: int, val):
        bucket = self.map[self.__get_hash(key)]

        for entry in bucket:
            if entry.key == key:
                entry.val = val
                return
        
        bucket.append(MapItem(key, val))

    def __ensure_resized(self):
        if len(self.map) < self.next_size:
            return
        
        self.temp = self.map

        self.map = [[]] * (self.next_size)
        self.next_size <<= 1

        for bucket in self.temp:
            for item in bucket:
                self.__add_or_update_item(item.key, item.val)
        
    def __get_hash(self, key: int):
        return key % len(self.map)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)