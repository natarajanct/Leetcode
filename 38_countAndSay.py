def countAndSay(n):  val: 111
    l = []
    for i in range(1,n+1):
	l.append(i)
    d = {}
    for item in l:
        d[item] = '1'
    for i in range(2,n+1):
        d[i] =

def val(str1):
    if len(str1) == 1:
        return '11'
    else:
        str = ''
        count = 1
        for i in range(1,len(str1)):
            if str1[i] == str1[i-1]:
                count+=1
            else:
                str(count)+str(str1[i-1])
                count = 1
                str(count)+str(str1[i])
                
        
