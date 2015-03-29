lines = open('rosalind_gc.txt')
gc = 0
l = 0
label = ""
maxgc = -1
maxlabel = ""
started = False

def num_gc(s):
    ct = 0
    for i in range(0, len(s)):
        if s[i] == 'C' or s[i] == 'G':
            ct += 1

    return ct

for line in lines:
    if line[0] == '>':
        if started and ((gc / l) > maxgc):
            maxgc = gc / l
            maxlabel = label
            gc = 0
            l = 0
        elif not started:
            started = True


        label = line
    else:
        gc += num_gc(line)
        l += len(line)

if gc/l > maxgc:
    maxgc = gc/l
    maxlabel = label

print(maxlabel)
print(str(maxgc))

