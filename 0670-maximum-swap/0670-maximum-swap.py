class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numstr=str(num)
        n=len(numstr)
        max_num=num
        for i in range(n):
            for j in range(i+1,n):
                num_list=list(numstr)
                num_list[i],num_list[j]=(
                    num_list[j],
                    num_list[i],
                )
                temp=int("".join(num_list))
                max_num=max(max_num,temp)
        return max_num