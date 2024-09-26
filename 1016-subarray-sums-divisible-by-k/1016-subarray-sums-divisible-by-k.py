class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=0
        prefix=0
        map=[0]*k
        map[0]=1
        for num in nums:
            prefix=(prefix+num%k+k)%k 
            res+=map[prefix]
            map[prefix]+=1
        return res