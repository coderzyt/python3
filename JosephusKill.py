class JosephusKill(object):

    def josephus_kill(self, head, m):
        if head is None or head.next is None or m < 1:
            return head

        last = head
        while last.next is not None:
            last = last.next

        count = 0
        while head != last:
            count = count + 1
            if count == m:
                last.next = head.next
                head = last.next
            else:
                last = last.next
                head = last.next

        return head