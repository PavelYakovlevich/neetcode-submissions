class TimeMap:

    def __init__(self):
        self.__dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.__dict:
            self.__dict[key] = []

        self.__dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.__dict:
            return ''
        
        target_entries = self.__dict.get(key)
        
        l, r = 0, len(target_entries) - 1
        res = ''

        while l <= r:
            m = (l + r) // 2

            if timestamp >= target_entries[m][0]:
                res = target_entries[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res
            
