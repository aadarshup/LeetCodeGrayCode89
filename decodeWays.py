def decodeways(s):
    ls = []
    ls.append(1)
    if s[0]!='0':
        ls.append(1)
    else:
        ls.append(0)
    for i in range(1,len(s)):
        first = int(s[i])
        second = int(s[i-1]+s[i])
        temp = 0
        if first>0 and first<=9:
            temp+=ls[i]
        if second>9 and second<=26:
            temp+=ls[i-1]
        ls.append(temp)
    return ls[len(ls)-1]
count = decodeways("1234569")
print(count)