class Solution(object):
    def areSentencesSimilar(self, s1, s2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        deque1=deque(s1.split())
        deque2=deque(s2.split())
        while deque1 and deque2 and deque1[0]==deque2[0]:
            deque1.popleft()
            deque2.popleft()
        while deque1 and deque2 and deque1[-1]==deque2[-1]:
            deque1.pop()
            deque2.pop()
        return not deque1 or not deque2        