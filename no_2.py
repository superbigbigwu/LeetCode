"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# date:2019.9.3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1.val + l2.val
        b = a % 10
        c = a // 10
        sum = ListNode(b)
        sum.next = ListNode(c)
        p1 = l1.next
        p2 = l2.next
        p3 = sum
        while True:
            if p1 and p2:
                a = p1.val + p2.val + p3.next.val
                b = a % 10
                c = a // 10
                p3.next.val = b
                p3.next.next = ListNode(c)
                p1 = p1.next
                p2 = p2.next
                p3 = p3.next
            elif p1 and not p2:
                a = p1.val + p3.next.val
                b = a % 10
                c = a // 10
                p3.next.val = b
                p3.next.next = ListNode(c)
                p1 = p1.next
                p3 = p3.next
            elif not p1 and p2:
                a = p2.val + p3.next.val
                b = a % 10
                c = a // 10
                p3.next.val = b
                p3.next.next = ListNode(c)
                p2 = p2.next
                p3 = p3.next
            else:
                if p3.next.val == 0:
                    p3.next = None
                break
        return sum