def hammingDistance(x, y):
        x_bin = DecToBin(x)
        y_bin = DecToBin(y)
        hd = 0
        if len(x_bin) < len(y_bin):
            x_bin = (len(y_bin)-len(x_bin))*'0' + x_bin
        else:
            y_bin = (len(x_bin)-len(y_bin))*'0' + y_bin
        print(x_bin)
        print(y_bin)
        for i in range(len(x_bin)):
            if int(y_bin[i]) ^ int(x_bin[i]) != 0:
                hd+=1
        return hd
    
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

print(DecToBin(1))
print(hammingDistance(3,1))
