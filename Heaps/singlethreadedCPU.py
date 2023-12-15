'''
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

'''
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #preserving original order of array before sorting them according to the enqeueuTime
        for i,task in enumerate(tasks):
            task.append(i)

        tasks.sort(key = lambda t : t[0])
        ans, minHeap = [], []
        #current task appended , current time
        i, time = 0 , tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap,[tasks[i][1],tasks[i][2]])
                i += 1
            
            if not minHeap:
                #fast forwading the time to the next enqueueTime
                time = tasks[i][0]

            else:
                processTime,index = heapq.heappop(minHeap)
                time += processTime
                ans.append(index)

        return ans