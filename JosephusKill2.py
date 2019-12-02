class JosephusKill2(object):

    def josephus_kill_2(self, head, m):
        if head is None or head.next is None or m < 1:
            return head
        cur = head.next
        tmp = 1
        while cur != head:
            tmp = tmp + 1
            cur = cur.next
        tmp = self.get_live(tmp, m)
        while (--tmp != 0):
            head = head.next
        head.next = head
        return head

    def get_live(self, i, m):
        if i == 1:
            return 1;
        return (self.get_live(i-1, m) + m - 1) % 1 + 1