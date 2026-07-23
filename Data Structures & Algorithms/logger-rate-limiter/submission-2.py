class Logger:

    def __init__(self):
        self.__entry_ttl = 10
        self.__map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        message_ttl = self.__map.get(message, 0)
        
        if timestamp < message_ttl:
            return False
        
        self.__map[message] = timestamp + self.__entry_ttl
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
