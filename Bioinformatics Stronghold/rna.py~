dnaF = open('rosalind_dna.txt')
mapping = {'A': 0, 'C' : 0, 'G' : 0, 'T' : 0}
for dna in dnaF:
    for i in range(0, len(dna)):
        if dna[i] in mapping.keys():
            mapping[ dna[i] ] += 1

print(str(mapping['A']) + " " + str(mapping['C']) + " " + str(mapping['G']) + " " + str(mapping['T']))
