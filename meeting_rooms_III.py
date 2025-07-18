import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Sort meetings by their start times
        meetings.sort()

        # Min-heap for available rooms (stores room indices)
        available_rooms = []
        for i in range(n):
            heapq.heappush(available_rooms, i)

        # Min-heap for occupied rooms (stores tuples: (finish_time, room_index))
        occupied_rooms = []

        # Array to store the count of meetings for each room
        meeting_counts = [0] * n

        for start, end in meetings:
            duration = end - start

            # Step 1: Free up rooms that have finished by 'start' time
            # While there are occupied rooms and the earliest finishing room has finished
            # before or at the current meeting's start time
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _finish_time, room_idx = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room_idx)

            # Step 2: Allocate the current meeting
            if available_rooms:
                # Case 1: Room is available
                room_idx = heapq.heappop(available_rooms)
                meeting_counts[room_idx] += 1
                heapq.heappush(occupied_rooms, (end, room_idx))
            else:
                # Case 2: No room available, meeting is delayed
                # Find the room that finishes earliest
                earliest_finish_time, room_idx = heapq.heappop(occupied_rooms)

                # The delayed meeting starts when this room becomes free
                new_start_time = earliest_finish_time
                new_end_time = new_start_time + duration

                meeting_counts[room_idx] += 1
                heapq.heappush(occupied_rooms, (new_end_time, room_idx))

        # Find the room that held the most meetings
        max_meetings = -1
        most_booked_room = -1

        for i in range(n):
            if meeting_counts[i] > max_meetings:
                max_meetings = meeting_counts[i]
                most_booked_room = i
            elif meeting_counts[i] == max_meetings:
                # If counts are equal, choose the room with the lowest number
                most_booked_room = min(most_booked_room, i) # This handles the tie-breaking implicitly since we iterate from 0 to n-1

        return most_booked_room