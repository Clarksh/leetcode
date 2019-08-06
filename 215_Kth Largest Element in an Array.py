class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 调整堆
        def adjust_heap(lists, i, size):#以i为根节点开始调整成以i为根节点的最大堆
            lchild = 2 * i + 1#堆是完全二叉树，可求左右子树
            rchild = 2 * i + 2
            max = i
            if i < size / 2:#完全二叉树的分支节点（就是有叶子节点的）小于等了size/2
                if lchild < size and lists[lchild] > lists[max]:
                    max = lchild
                if rchild < size and lists[rchild] > lists[max]:
                    max = rchild
                if max != i:#如果根节点不是最大就调换位置
                    lists[max], lists[i] = lists[i], lists[max]
                    adjust_heap(lists, max, size)#然后以max为根节点进行调整

        # 创建堆
        def build_heap(lists, size):#从下往上构建堆
            for i in range(0, int(size/2))[::-1]:
                adjust_heap(lists, i, size)
        
        size = len(nums)
        build_heap(nums,size)#先创建堆
        count = 0
        for i in range(0, size)[::-1]:#i从size-1到1
            nums[0], nums[i] = nums[i], nums[0]#交换堆顶和堆底
            count += 1 #获得一个最大值加1
            if count == k:
                #print(nums[i])
                return nums[i]
            adjust_heap(nums, 0, i)#把剩下的重新排