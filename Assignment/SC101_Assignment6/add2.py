"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(l1.val + l2.val, None)
    if l1.next is None:  # 只有個位數
        cur_n1 = ListNode(0, None)
    else:
        cur_n1 = l1.next
    if l2.next is None:  # 只有個位數
        cur_n2 = ListNode(0, None)
    else:
        cur_n2 = l2.next
    add_pre = head

    while cur_n1.next is not None or cur_n2.next is not None:
        add_cur = ListNode(cur_n1.val + cur_n2.val, None)
        add_pre.next = add_cur
        if add_pre.val >= 10:  # 確認進位
            add_pre.val -= 10
            add_cur.val += 1
        # move to next node
        add_pre = add_cur
        if cur_n1.next is None:  # this is the last node in l1 linked list
            cur_n1.val = 0
        else:
            cur_n1 = cur_n1.next
        if cur_n2.next is None:  # this is the last node in l2 linked list
            cur_n2.val = 0
        else:
            cur_n2 = cur_n2.next

    # OBOB case
    add_cur = ListNode(cur_n1.val + cur_n2.val, None)
    add_pre.next = add_cur
    if add_pre.val >= 10:  # 確認進位
        add_pre.val -= 10
        add_cur.val += 1

    # 確認最高位是否進位
    if add_cur.val >= 10:
        add_cur.val -= 10
        add_cur.next = ListNode(1, None)

    return head


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
