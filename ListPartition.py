from Node import Node


class ListPartition(object):

    def list_paitition2(self, head: Node, pivot:int) -> Node:
        if head is None:
            return head

        small_head = None
        small_tail = None
        equal_head = None
        equal_tail = None
        big_head = None
        big_tail = None
        next = None
        while head is not None:
            next = head.next
            head.next = None
            if head.value < pivot:
                if small_head is None:
                    small_head = head
                    small_tail = head
                else:
                    small_tail.next = head
                    small_tail = head
            elif head.value == pivot:
                if equal_head is None:
                    equal_head = head
                    equal_tail = head
                else:
                    equal_tail.next = head
                    equal_tail = head
            else:
                if big_head is None:
                    big_head = head
                    big_tail = head
                else:
                    big_tail.next = head
                    big_tail = head
            head = next

        if small_tail is not None:
            small_tail.next = equal_head
            equal_tail = small_tail if equal_tail is None else equal_tail

        if equal_tail is not None:
            equal_tail.next = big_head

        return small_head if small_head is not None else (equal_head if equal_head is not None else big_head)

    def list_partition(self, head: Node, pivot: int) -> Node:
        if head is None:
            return head
        cur = head
        length = 0
        while cur is not None:
            length = length + 1
            cur = cur.next

        arr_node = [Node]
        cur = head
        while cur is not None:
            arr_node.append(cur)
            cur = cur.next

        self.arr_partition(arr_node, pivot)
        i = 1
        while i != arr_node.__len__():
            arr_node[i - 1].next = arr_node[i]
        arr_node[i - 1].next = None
        return arr_node[0]

    def swap(self, node_arr: list, a: int, b: int):
        tmp = node_arr[a]
        node_arr[a] = node_arr[b]
        node_arr[b] = tmp

    def arr_partition(self, node_arr: list, pivot: int):
        small = -1
        big = node_arr.__len__()
        index = 0
        while index != big:
            if node_arr[index] < pivot:
                small = small + 1
                self.swap(node_arr, small, index)
                index = index + 1
            elif node_arr[index] == pivot:
                index = index + 1
            else:
                big = big - 1
                self.swap(node_arr, big, index)


