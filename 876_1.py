# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class linked_list(object):
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return       
    
    def create_ll_from_list(self,ls):
        for item in ls:
            self.append(item)
           

    def display(self):
        if not self.head:
            return linked_list()
        current = self.head
        while current:
            print(current.val )
            current = current.next
                  

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count = 0
        temp_ls = []
        while head:
            count += 1
            temp_ls.append(head.val)
            head = head.next
        return temp_ls[int(count/2)]    
            
        


# head_ls = [1,2,3,4,5]
head_ls = [1,2,3,4,5,6]
linked_list_obj = linked_list()
# linked_list_obj.append(1)
# linked_list_obj.append(2)
# linked_list_obj.append(1)
linked_list_obj.create_ll_from_list(head_ls)

# linked_list_obj.display()
solution = Solution()
middle = solution.middleNode(linked_list_obj.head)        
print(f"{middle=}")