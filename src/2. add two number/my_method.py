from typing import Optional
from functools import reduce


# Provided to us
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def break_list(self, _list: ListNode, carry: list) -> None:
        carry.append(_list.val)

        if list_next := _list.next:
            self.break_list(list_next, carry)

    def number_to_linked_list(self, number: int) -> ListNode:
        for_list = list(map(int, str(number)))
        index = 0

        carry_node: ListNode = ListNode()
        while True:
            try:
                item = for_list[index]
            except IndexError:
                break

            list_node = ListNode()
            list_node.val = item

            if index == 0:
                list_node.next = None
            else:
                list_node.next = carry_node

            carry_node = list_node
            index += 1

        return carry_node

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        list_1 = []
        list_2 = []

        self.break_list(l1, list_1)
        self.break_list(l2, list_2)

        first_number = int("".join(str(num) for num in reversed(list_1)))
        second_number = int("".join(str(num) for num in reversed(list_2)))

        linked_list = first_number + second_number

        return self.number_to_linked_list(linked_list)


# solution_1 = Solution().addTwoNumbers(
#     l1=ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None))),
#     l2=ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None))),
# )
# solution_2 = Solution().addTwoNumbers(
#     l1=ListNode(val=0, next=None),
#     l2=ListNode(val=0, next=None),
# )
# solution_3 = Solution().addTwoNumbers(
#     l2=ListNode(2, ListNode(4, ListNode(9, None))),
#     l1=ListNode(5, ListNode(6, ListNode(4, ListNode(9, None)))),
# )
