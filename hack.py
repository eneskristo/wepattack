class Hack:
    def __init__(self, ivsize, keyLength, charsize, byteone):
        self.ivsize = ivsize
        self.keyLength = keyLength
        self.charsize = charsize
        self.byteone = ord(byteone)
        self.Packets = []

    def getPacket(self, p):
        self.Packets.append(p)

    def solveWEP(self):
        # Uses current packets to try and solve WEP
        key = [None] * (self.ivsize + self.keyLength)
        for k in range(self.keyLength):
            prob = [0] * self.charsize
            for packet in self.Packets:
                for iv in range(self.ivsize):
                    key[iv] = ord(packet[iv])
                S = [x for x in range(self.charsize)]
                i = 0
                j = 0
                while i < k + self.ivsize:
                    j = (j + S[i] + key[i])%self.charsize
                    helper = S[i]
                    S[i] = S[j]
                    S[j] = helper
                    i+=1
                if S[1]+S[S[1]] == i and S[1] < self.ivsize:
                    byte = ord(packet[self.ivsize]) ^ self.byteone
                    keyByte = (byte - j - S[i]) % 256
                    prob[keyByte] += 1
            key[self.ivsize+k] = prob.index(max(prob))
        return [chr(x) for x in key[self.ivsize:]]

