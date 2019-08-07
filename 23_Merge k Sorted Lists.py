# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        num = len(lists)  # 遍历数组，看有多少有序链表
        if num == 1:
            return lists[0]
        mid = int(num / 2)
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge2Lists(left, right)

    def merge2Lists(self, left, right):  # 将两个有序链表合成一个有序链表
        if not left: return right
        if not right: return left
        if left.val < right.val:
            left.next = self.merge2Lists(left.next, right)
            return left
        else:
            right.next = self.merge2Lists(left, right.next)
            return right