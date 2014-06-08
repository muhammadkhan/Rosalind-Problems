lines = open('rosalind_ini5.txt')
lineNum = 1
for l in lines:
    if lineNum % 2 == 0:
        print(l)
    
    lineNum += 1
