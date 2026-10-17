import heapq

class Solution:
    def minMeetingRooms(self, start, end):
        n = len(start)
        meetings = [ (start[i], end[i]) for i in range(n) ]
        
        meetings.sort(key = lambda x: x[0])
        
        rooms = []
        i = 0
        result = 0
        
        while i < n:
            
            while len(rooms) and rooms[0] <= meetings[i][0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, meetings[i][1])
            
            result = max(result, len(rooms))
            
            i += 1
        
        return result