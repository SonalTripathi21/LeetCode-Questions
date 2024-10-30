class Solution(object):
    def getLongestIncreasingSubsequenceLength(self, v):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis_len=[1]*len(v)
        lis=[v[0]]
        for i in range(1,len(v)):
            index=self.lowerBound(lis,v[i])
            if index==len(lis):
                lis.append(v[i])
            else:
                lis[index]=v[i]
            lis_len[i]=len(lis)
        return lis_len
    def lowerBound(slef,lis,target):
        left,right=0,len(lis)
        while left<right:
            mid=left+(right-left)//2
            if lis[mid]<target:
                left=mid+1
            else:
                right=mid
        return left
    def minimumMountainRemovals(self,nums):
        N=len(nums)
        lis_length=self.getLongestIncreasingSubsequenceLength(nums)
        nums.reverse()
        lds_length=self.getLongestIncreasingSubsequenceLength(nums)
        lds_length.reverse()
        min_removals=float("inf")
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(
                    min_removals, N - lis_length[i] - lds_length[i] + 1
                )

        return min_removals