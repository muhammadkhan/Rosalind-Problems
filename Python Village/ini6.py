lines = open('rosalind_ini6.txt')
dic = {}
for l in lines:
    l_split = l.split()
    for word in l_split:
        if word in list(dic.keys()):
            dic[word] += 1
        else:
            dic[word] = 1


for k in dic.keys():
    print(k + " " + str(dic[k]))
