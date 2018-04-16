def strStr(self, haystack, needle):
    if len(needle)==0:
        return 0
    elif needle in haystack:
        for i in range(len(haystack)):
            if(haystack[i:i+len(needle)]==needle):
                return i
    else:
        return -1
