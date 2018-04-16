def reverseString(self, s):
    op = ''
    for i in range(len(s)-1,-1,-1):
       op = op+s[i]
    return op
