import copy
test = [0,1,0]
test2 = copy.deepcopy(test)

i = len(test)-1
j = len(test)-1
res = 0
while i >= 0:
    if test[i] == 0:
        i -= 1
    elif test[i] == 1 and test[j] == 1:
        i-=1
        j-=1
    elif test[i] == 1:
        res += j-i
        temp = test[j]
        test[j] = test[i]
        test[i] = temp
        j -= 1

i = 0
j = 0
ret = 0
while i < len(test):
    if test2[i] == 0:
        i += 1
    elif test2[i] == 1 and test2[j] == 1:
        i += 1
        j += 1
    elif test2[i] == 1:
        ret += i - j
        temp = test2[j]
        test2[j] = test2[i]
        test2[i] = temp
        j += 1

print(ret)