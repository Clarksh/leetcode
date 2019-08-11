class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        # result[0] = []
        # if len(num) == 0:
        #     return result
        for i in range(0,len(nums)):
            # 添加 新元素 和之前旧元素的集合
            result = result + [[nums[i]] + j for j in result]
        return result