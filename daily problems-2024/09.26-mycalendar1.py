# You are implementing a program to use as your calendar. 
# We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection 
# (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers start and end that 
# represents a booking on the half-open interval [start, end), 
# the range of real numbers x such that start <= x < end.


class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.intervals:
            if e > start and s < end:
                return False
        self.intervals.append((start, end))
        return True
