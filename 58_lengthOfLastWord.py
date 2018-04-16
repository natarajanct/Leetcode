def lengthOfLastWord(s):
        b = s.split(' ')
        for i in range(len(b)-1,-1,-1):
            if b[i] == '':
                continue
            return len(b[i])
            
        return len(b[len(b)-1])

print(lengthOfLastWord('    '))
