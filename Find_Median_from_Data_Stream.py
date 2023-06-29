class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        
    def addNum(self, num: int) -> None:
        heappush(self.low, -num)
        heappush(self.high, -self.low[0])
        heappop(self.low)

        if len(self.low) < len(self.high):
            heappush(self.low, -self.high[0])
            heappop(self.high)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (self.high[0] - self.low[0]) / 2