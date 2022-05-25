import re
import os
# import these two functions
os.chdir("C:/Users/lenovo/Desktop")
# I arrived at the location of this file in my computer.
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
# This code is used to read this file.
D1 = {}
# I created a new dictionary and named it D1.
for line in file:
    line = line.rstrip()
# Store the string from the original file.
    if line.startswith('>'):
        genes = re.search(r'gene:(.+?\s)', line)
        genes_seq = '\n' + '>' + genes.group(1)# Find the gene names and store them in a new list called genes_seq.
        D1[genes_seq] = " "
    else:
        D1[genes_seq] = D1[genes_seq] + line # Putting gene sequences into my dictionary.
output_file = open('cut_genes.fa', 'w')
# Name my output file and change it to writable mode.
for n in D1.keys():
    if re.search('GAATTC',D1[n]):
        target_DNA = re.findall('GAATTC', D1[n])
        length = str(len(D1[n]))
# Caculate the length.
        DNA_and_length = n + " " + length
        DNA_and_number = DNA_and_length.strip()
# Find sequences containing at least one EcoRI recognition site.
        output_file.write(DNA_and_length + D1[n] + '\n')