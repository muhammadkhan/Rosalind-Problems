def complement(c):
    if c == 'A':
        return 'T'
    elif c == 'T':
        return 'A'
    elif c == 'C':
        return 'G'
    elif c == 'G':
        return 'C'
    else:
        return ''


data = open("rosalind_revc.txt")
for template in data:
    t = list(template)
    for i in range(0, len(t)):
        t[i] = complement(t[i])

    t.reverse()
    print("".join(t))
