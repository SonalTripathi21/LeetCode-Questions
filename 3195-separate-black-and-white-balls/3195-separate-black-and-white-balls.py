class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_swaps=0
        black_ball_count=0
        for char in s:
            if char=="0":
                total_swaps+=black_ball_count
            else:
                black_ball_count+=1
        return total_swaps
        