from Node import Node

class NodeIsPalindrome(object):

    def is_palindrome(self, head: Node) -> bool:
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur)
            cur = cur.next
        while head is not None:
            if head.value != stack.pop().value:
                return False
            head = head.next
        return True

    def is_palindrome2(self, head: Node) -> bool:
        stack = []
        if head is None or head.next is None:
            return head

        cur = head
        right = head.next
        while cur.next is not None and cur.next.next is not None:
            right = right.next
            cur = cur.next.next

        while right is not None:
            stack.append(right)
            right = right.next
        while stack.__len__() != 0:
            if stack.pop().value != head.value:
                return False
            head = head.next

        return True

if __name__ == '__main__':
    node6 = Node(1, None)
    node5 = Node(2, node6)
    node4 = Node(3, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    isPalindrome = NodeIsPalindrome()
    print(isPalindrome.is_palindrome2(node1))