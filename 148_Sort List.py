class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next): return head
        fast, slow = head.next, head  #
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next  # 遍历时候 快指针走两步，慢指针走一步
        # 当快指针走到终点，慢指针就到中点，截断链表
        mid, slow.next = slow, None
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge2Lists(left, right)

    def merge2Lists(self, left: ListNode, right: ListNode) -> ListNode:
        if not left: return right
        if not right: return left
        if left.val < right.val:
            left.next = self.merge2Lists(left.next, right)
            return left
        else:
            right.next = self.merge2Lists(left, right.next)
            return right