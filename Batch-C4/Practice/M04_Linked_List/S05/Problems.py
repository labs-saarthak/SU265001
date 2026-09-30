#Leet Code - 206:
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        '''prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
        return prev'''
        #2nd Approach
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
        
#Leet Code - 141:
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False'''
        #2nd Approach
        a = set()
        curr = head
        while curr:
            if curr in a:
                return True
            a.add(curr)
            curr = curr.next
        return False

#Leet Code - 21:
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
        
# Leet Code -19:
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        '''dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next 
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next'''
        #2nd Approach
        length = 0
        curr =head
        while curr:
            length += 1
            curr = curr.next
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        for i in range(length - n):
            curr = curr.next 
        curr.next = curr.next.next
        return dummy.next      

#Leet Code - 876:
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        '''length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        curr = head
        for i in range(length // 2):
            curr = curr.next
        return curr'''
        #2nd Approach
        '''nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        return nodes[len(nodes) // 2]'''
        #3rd Approach
        slow =head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        






        
