import heapq


class Solution:
    def minMeetingRooms(self, intervals):

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        free_rooms = []

        heapq.heappush(free_rooms, intervals[0][1])

        for (s, e) in intervals[1:]:

            if s >= free_rooms[0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, e)

        return len(free_rooms)


intervals = [[0, 30], [5, 10], [15, 20]]
ans = Solution().minMeetingRooms(intervals)
print(ans)
