class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        n=len(skill)
        total_chemistry=0
        target_team_skill=skill[0]+skill[-1]
        for i in range(n//2):
            if skill[i]+skill[-i-1]!=target_team_skill:
                return -1
            total_chemistry+=skill[i]*skill[-i-1]
        return total_chemistry