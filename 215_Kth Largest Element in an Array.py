class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # ������
        def adjust_heap(lists, i, size):#��iΪ���ڵ㿪ʼ��������iΪ���ڵ������
            lchild = 2 * i + 1#������ȫ��������������������
            rchild = 2 * i + 2
            max = i
            if i < size / 2:#��ȫ�������ķ�֧�ڵ㣨������Ҷ�ӽڵ�ģ�С�ڵ���size/2
                if lchild < size and lists[lchild] > lists[max]:
                    max = lchild
                if rchild < size and lists[rchild] > lists[max]:
                    max = rchild
                if max != i:#������ڵ㲻�����͵���λ��
                    lists[max], lists[i] = lists[i], lists[max]
                    adjust_heap(lists, max, size)#Ȼ����maxΪ���ڵ���е���

        # ������
        def build_heap(lists, size):#�������Ϲ�����
            for i in range(0, int(size/2))[::-1]:
                adjust_heap(lists, i, size)
        
        size = len(nums)
        build_heap(nums,size)#�ȴ�����
        count = 0
        for i in range(0, size)[::-1]:#i��size-1��1
            nums[0], nums[i] = nums[i], nums[0]#�����Ѷ��Ͷѵ�
            count += 1 #���һ�����ֵ��1
            if count == k:
                #print(nums[i])
                return nums[i]
            adjust_heap(nums, 0, i)#��ʣ�µ�������