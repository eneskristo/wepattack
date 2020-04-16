import random


class Router:

    def __init__(self, N, key):
        self.S = []
        self.N = N
        self.key = key
        self.counter = 0

    def getIV(self):
        return [self.counter % 256]

    def getKey(self):
        return self.key

    def RC4(self, n, iv):
        self.S = [x for x in range(self.N)]
        iv.extend(self.getKey())
        self.KSA(iv)
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
        encrpyt = self.RC4(l, self.getIV())
        newmessage = [chr(x) for x in self.getIV()]
        newmessage.extend([chr(ord(message[i]) ^ encrpyt[i]) for i in range(l)])
        return newmessage

    def decrypt(self, message):
        decrypt = self.RC4(len(message)-len(self.getIV()), [ord(x) for x in message[:len(self.getIV())]])
        newmessage = [chr(ord(message[i]) ^ decrypt[i-1]) for i in range(1,len(message))]
        return newmessage

    def checkSum(self, message):
        return str(len(message))
