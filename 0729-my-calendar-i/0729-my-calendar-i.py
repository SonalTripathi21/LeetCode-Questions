class MyCalendar(object):

    def __init__(self):
        self.booking=[]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for existingStart,existingEnd in self.booking:
            if start<existingEnd and end>existingStart:
                return False
        self.booking.append((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)