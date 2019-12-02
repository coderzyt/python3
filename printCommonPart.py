from Node import Node

class printCommonPart(object):
    def print_common_part(self, head1: Node, head2: Node):
        while head1 is not None and head2 is not None:
            if head1.value < head2.value:
                head1 = head1.next
            elif head1.value > head2.value:
                head2 = head2.next
            else:
                print(head1.value)
                head1 = head1.next
                head2 = head2.next
        # print('\n')

if __name__ == '__main__':
    node3 = Node(3, None)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    node6 = Node(4, None)
    node5 = Node(3, node6)
    node4 = Node(2, node5)

    printCommonPart = printCommonPart()
    printCommonPart.print_common_part(node1, node4)




