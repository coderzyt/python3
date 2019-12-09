class NodeRand(object):

    def __init__(self, value, next, rand):
        self.value = value
        self.next = next
        self.rand = rand

    def __str__(self) -> str:
        return str(self.value) + "-----" + str(self.rand) + "\n" + "-----" + str(self.next)