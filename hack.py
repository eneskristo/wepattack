class Hack:
    def __init__(self):
        self.Packets = []

    def getPackets(self, p):
        self.Packets.extend(p)

    def solveWEP(self, n):
        Key = [0] * n
