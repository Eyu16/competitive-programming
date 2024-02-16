class FrequencyTracker:

    def __init__(self):
        self.tracker = defaultdict(int)
        self.frequency_counter = defaultdict(int)
        

    def add(self, number: int) -> None:
        if number in self.tracker:
            prev_fr = self.tracker[number]
            self.frequency_counter[prev_fr] -= 1
            self.tracker[number] += 1
            self.frequency_counter[self.tracker[number]] += 1
        else:
            self.tracker[number] += 1
            self.frequency_counter[self.tracker[number]] += 1
        
    def deleteOne(self, number: int) -> None:
        if number in self.tracker and self.tracker[number] > 0:
            prev_fr = self.tracker[number]
            self.frequency_counter[prev_fr] -= 1
            self.tracker[number] -= 1
            if self.tracker[number] > 0:
                self.frequency_counter[self.tracker[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.frequency_counter:
            if self.frequency_counter[frequency] != 0:
                return True
        return False



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)