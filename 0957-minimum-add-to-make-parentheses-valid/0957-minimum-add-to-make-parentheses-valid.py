class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_brackets=0
        min_adds_required=0
        for c in s:
            if c=="(":
                open_brackets+=1
            else:
                if open_brackets>0:
                    open_brackets-=1
                else:
                    min_adds_required+=1
        return min_adds_required+open_brackets

        