def generateRepetitionCode(r, messageBits):
    repeatedMessageBits = []
    for i in messageBits:
        n = r
        while n > 0:
            repeatedMessageBits.append(i)
            n-=1
    return repeatedMessageBits
