from DoubleNode import DoubleNode
from Node import Node


class RemoveK(object):

    def remove_k_from_doubleNode(self, doubleNode, k):
        if doubleNode is None or k <= 0:
            return doubleNode
        while doubleNode.next is not None:
            doubleNode = doubleNode.next
        while k - 1 > 0:
            if doubleNode.pre is None:
                return None
            doubleNode = doubleNode.pre
            k = k - 1
        return doubleNode

    def remove_k_from_node(self, node, k):
        head = node
        if node is None or k <= 0:
            return node
        while node is not None:
            node = node.next
            k = k - 1
        if k == 0:
            return head
        elif k > 0:
            print('node has no reciprocal k element')
            return None
        else:
            for i in range(1, -k + 1):
                head = head.next
            return head

if __name__ == '__main__':
    # node6 = Node(4, None)
    # node5 = Node(3, node6)
    # node4 = Node(2, node5)
    # node3 = Node(3, node4)
    # node2 = Node(2, node3)
    # node1 = Node(1, node2)

    removeK = RemoveK()
    # print(removeK.remove_k_from_node(node1, 6).value)

    node6 = DoubleNode(6)
    node5 = DoubleNode(5)
    node4 = DoubleNode(4)
    node3 = DoubleNode(3)
    node2 = DoubleNode(2)
    node1 = DoubleNode(1)

    node1.set_pre(None)
    node1.set_next(node2)

    node2.set_pre(node1)
    node2.set_next(node3)

    node3.set_pre(node2)
    node3.set_next(node4)

    node4.set_pre(node3)
    node4.set_next(node5)

    node5.set_pre(node4)
    node5.set_next(node6)

    node6.set_pre(node5)
    node6.set_next(None)

    print(removeK.remove_k_from_doubleNode(node1, 0).value)