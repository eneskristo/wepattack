import random


class Router:

    def __init__(self, N, key):
        self.S = [x for x in range(N)]
        self.N = N
        self.key = key
        self.counter = 0

    def getIV(self):
        return [self.counter % 256]

    def newKey(self):
        toReturn = []
        toReturn.extend(self.getIV())
        toReturn.extend(self.key)
        return toReturn

    def RC4(self, n):
        cKey = self.newKey()
        self.KSA(cKey)
        return self.PRGA(n)

    def KSA(self, key):
        j = 0
        for i in range(self.N):
            j = (j + self.S[i] + key[i % len(key)]) % self.N
            helper = self.S[i]
            self.S[i] = self.S[j]
            self.S[j] = helper

    def PRGA(self, n):
        i = 0
        j = 0
        toReturn = [0] * n
        for z in range(n):
            i = (i + 1) % self.N
            j = (j + self.S[i]) % self.N
            helper = self.S[i]
            self.S[i] = self.S[j]
            self.S[j] = helper
            toReturn[z] = self.S[(self.S[i] + self.S[j]) % self.N]
        return toReturn

    def encrypt(self, message):
        self.counter += 1
        message = message + self.checkSum(message)
        l = len(message)
        encrpyt = self.RC4(l)
        newmessage = [chr(x) for x in self.getIV()]
        newmessage.extend([chr(ord(message[i]) ^ encrpyt[i]) for i in range(l)])
        return newmessage

    def checkSum(self, message):
        return str(len(message))
