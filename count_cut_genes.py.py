import re
# Import re function
file_name = input('Give this file a name:')
# let users name the file.
output_file = open(file_name, 'w')
origin_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
# Make the file 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa' as a reading one.
D1 = {}
# Set up a new dictionary named D1
for line in origin_file:
    line = line.rstrip()
    if line.startswith('>'):
        gene = re.search(r'gene:(.+?\s)', line)
# Search for the genes' names in the line
        gene_seq = '\n' + '>' + gene.group(1)
        D1[gene_seq] = " "
# The codes means:if the line is the genes' name, it will become a white space.
    else:
        D1[gene_seq] = D1[gene_seq] + line
# Similar to the previous step: If the line is genes' sequence, it will be put into the dirtionary.
for i in D1.keys():
# i represents the gene lines
    if re.search('GAATTC',D1[i]):
        target_DNA = re.findall('GAATTC', D1[i])
# So,if "GAATTC" can be searched for in this order, this section will be selected.
        fragment = str(len(D1[i]) + 1)
# Calculate the final selected DNA fragment.
        DNA_and_fragment = i + " " + fragment
        DNA_and_number = DNA_and_fragment.strip()
        output_file.write(DNA_and_number + D1[i] + '\n')
# Finally,output the genes' names, fragments and sequences.