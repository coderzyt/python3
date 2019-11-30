from mpmath import ceil


class RemoveMiddleNode(object):

    def removeMidNode(self, node):
        if node.value is None or node.next is None:
            return node
        if node.next.next is None:
            return node

        pre = node
        cur = node.next.next
        while pre.next is not None and cur.next.next is not None:
            pre = pre.next
            cur = cur.next.next
        pre.next = pre.next.next
        return node

    def removeByRatio(self, head, a, b):
        if a < 1 or a > b:
            return head
        if head is None:
            return head
        cur = head
        n = 1
        while cur.next is not None:
            n = n + 1
            cur = cur.next

        ratio = ceil(float(a / b))

        if ratio == 1:
            head = head.next

        if ratio > 0:
            cur = head
            while --ratio != 1:
                cur = cur.next
            cur.next = cur.next.next
        return head

if __name__ == '__main__':
    print(2 // 4)








