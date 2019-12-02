from Node import Node


class ReverseListNoe(object):

    def reverseListNoe(self, head: Node) -> Node:
        if head is None or head.next is None:
            return head

        pre = None
        next = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

if __name__ == '__main__':
    node6 = Node(6, None)
    node5 = Node(5, node6)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    print(node1)
    reverseListNode = ReverseListNoe()
    print(reverseListNode.reverseListNoe(node1))
