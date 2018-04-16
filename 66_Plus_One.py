def plusOne(digits):
    if len(digits) == 0:
        return [0]
    s = ''
    for num in digits:
        s = s + str(num)
    ans = int(s)+ 1
    ans = str(ans)
    op = []
    for i in range(len(ans)):
        op.append(int(ans[i]))
    return op
print(plusOne([]))
        
        
