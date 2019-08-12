class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums) #去重
        nums_dict = {}
        for i in nums_set:#初始化计数器
            nums_dict.update({i:0})
    #     print(nums_dict)
        for j in nums:
            nums_dict[j] += 1
    #     print(nums_dict)
        for j in nums_set:
            if nums_dict[j] == 1 :
                return j