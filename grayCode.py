def graycode(n):
    if n==1:
        return [0,1]
    prev=[]
    prev = graycode(n-1)
    max=0
    for i in prev:
        if max<i:
            max=i
    result = []
    for i in prev:
        result.append(i)
    for i in range(len(prev)-1,-1,-1):
        result.append(max+1+prev[i])
    return result

finallist = graycode(3)
print(finallist)