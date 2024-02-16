class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.result = [""] * n
        self.p = 0
        
        

    def insert(self, idKey: int, value: str) -> List[str]:
        l = []
        self.result[idKey - 1] = value
        for i in range(self.p, len(self.result)):
            if self.result[i] != "":
                l.append(self.result[i])
            else:
                break
        self.p = i
        return l
            
        
        
        
        
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)