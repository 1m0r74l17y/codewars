def tobase64(text):
    binarys = '0' + '0'.join(format(ord(x), 'b') for x in text)
    binary6 = [binarys[i:i+6] for i in range(0, len(binarys), 6)]

    return binary6

print tobase64("Man")
