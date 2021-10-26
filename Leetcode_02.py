# def addTwoNumbers(l1, l2):
#
#     ans = []
#     remainder = 0
#     if len(l2) > len(l1):
#         l1,l2 = l2,l1
#     n1, n2 = len(l1), len(l2)
#     for i in range(n2):
#         el = l1[i] + l2[i] + remainder
#         ans.append(el % 10)
#         remainder = el // 10
#     for i in range(n2, n1):
#         el = l1[i] + remainder
#         ans.append(el % 10)
#         remainder = el // 10
#     if remainder:
#         ans.append(1)
#     return ans


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(addTwoNumbers(l1,l2))