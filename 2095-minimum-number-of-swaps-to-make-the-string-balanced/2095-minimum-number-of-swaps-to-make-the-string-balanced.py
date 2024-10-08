class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=deque()
        unbalanced=0
        for ch in s:
            if ch=="[":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    unbalanced+=1
        return (unbalanced+1)//2
        