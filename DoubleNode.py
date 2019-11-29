class DoubleNode(object):

    def __init__(self, value):
        self.value = value
        self.pre = None
        self.next = None

    def set_pre(self, pre):
        self.pre = pre

    def set_next(self, next):
        self.next = next
