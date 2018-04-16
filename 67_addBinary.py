def addBinary(a, b):
    return (DecToBin(BinToDec(a)+BinToDec(b)))
    
def BinToDec(a):
    if int(a)<2:
        print(int(a))
        return int(a)
    val = 0
    i = 0
    j = len(a)-1
    while(i<len(a) and j>=0):
        val = val + int(a[i])*(2**j)
        i+=1
        j-=1
    print(val)
    return val

def DecToBin(a):
    strval = ''
    val = ''
    while(a>1):
        val = val + str(a%2)
        a = a//2
    val = val + str(a)
    for i in range(len(val)-1,-1,-1):
        strval = strval + val[i]
    return strval

print(addBinary('11','1'))


        
        
        
