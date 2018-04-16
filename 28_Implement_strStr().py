def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    elif needle in haystack:
        for i in range(len(haystack)):
            count = 0
            if haystack[i]==needle[0]:
                count+=1
                for j in range(1,len(needle)):
                    if haystack[i+j]==needle[j]:
                        count+=1
            if count == len(needle):
                return i
    else:
        return -1

haystack = ''
needle = 'a'
val = strStr(haystack, needle)
print(val)
