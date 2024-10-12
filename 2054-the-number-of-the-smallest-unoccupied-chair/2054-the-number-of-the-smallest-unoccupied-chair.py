class Solution:
    def smallestChair(self, times, targetFriend):
        target_arrival = times[targetFriend][0]
        times = sorted(
            [
                (arrival, leave, index)
                for index, (arrival, leave) in enumerate(times)
            ]
        )

        next_chair = 0
        available_chairs = []
        leaving_queue = []

        for time in times:
            arrival, leave, index = time

            # Free up chairs based on current time
            while leaving_queue and leaving_queue[0][0] <= arrival:
                _, chair = heapq.heappop(leaving_queue)
                heapq.heappush(available_chairs, chair)

            if available_chairs:
                current_chair = heapq.heappop(available_chairs)
            else:
                current_chair = next_chair
                next_chair += 1

            # Push current leave time and chair
            heapq.heappush(leaving_queue, (leave, current_chair))

            # Check if it's the target friend
            if index == targetFriend:
                return current_chair

        return 0