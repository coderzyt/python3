from Node import Node


class NodeIsPalindrome(object):

    def is_palindrome(self, head: Node) -> bool:
        if head is None:
            return False
        if head == head.next:
            return True
        cur1 = head
        cur2 = head
        while cur2 is not None:
            cur1 = cur1.next
            cur2 = cur2.next.next
            if cur1 == cur2:
                return True
        return False

if __name__ == '__main__':
    node6 = Node(6, None)
    node5 = Node(5, node6)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)