class MedianFinder:

    def __init__(self):
        self.__small_heap = []
        self.__big_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.__small_heap, num)

        if ((self.__small_heap and self.__big_heap) and (self.__small_heap[0] > self.__big_heap[0])):
            max_smallest_val = heapq.heappop_max(self.__small_heap)
            heapq.heappush(self.__big_heap, max_smallest_val)

        if len(self.__small_heap) - len(self.__big_heap) > 1:
            max_smallest_val = heapq.heappop_max(self.__small_heap)
            heapq.heappush(self.__big_heap, max_smallest_val)
        
        if len(self.__big_heap) - len(self.__small_heap) > 1:
            min_greatest_val = heapq.heappop(self.__big_heap)
            heapq.heappush_max(self.__small_heap, min_greatest_val)

    def findMedian(self) -> float:
        if len(self.__big_heap) > len(self.__small_heap):
            return self.__big_heap[0]
        elif len(self.__small_heap) > len(self.__big_heap):
            return self.__small_heap[0]
        else:
            return (self.__small_heap[0] + self.__big_heap[0]) / 2
        
        
        