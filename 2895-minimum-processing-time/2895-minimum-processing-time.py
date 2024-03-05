class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        max_process = []
        tasks.sort()
        processorTime.sort(reverse=True)
        max_process.append(tasks[3])
        for i in range(7, len(tasks), 4):
            max_process.append(tasks[i])
        min_time = 0
        i = 0
        while i < len(processorTime):
            min_time = max(processorTime[i]+max_process[i], min_time)
            i += 1
        return min_time
