import pandas as pd
import re
# Import the re and numpy function.
sequence = ''
# A newly defined function is used to select the amino sequence from the lines in the file.
def read_file(file):
    for lines in file:
        if not lines.startswith('>'):
            sequence = lines
    sequence = re.sub(r'\s+','', sequence)
    sequence = re.sub(r'\n','', sequence)
    return sequence
file1 = read_file(open('DLX5_human.fa'))
print(file1)
file2 = read_file(open('DLX5_mouse.fa'))
print(file2)
file3 = read_file(open('RandomSeq(1).fa'))
print(file3)
# DNA sequences were extracted from 3 files.
BLOSUM = {'A':[4,-1,-2,-2,0,-1,-1,0,-2,-1,-1,-1,-1,-2,-1,1,0,-3,-2,0,-2,-1,0,-4],'R':[-1,5,0,-2,-3,1,0,-2,0,-3,-2,2,-1,-3,-2,-1,-1,-3,-2,-3,-1,0,-1,-4],
           'N':[-2,0,6,1,-3,0,0,0,1,-3,-3,0,-2,-3,-2,1,0,-4,-2,-3,3,0,-1,-4],'D':[-2,-2,1,6,-3,0,2,-1,-1,-3,-4,-1,-3,-3,-1,0,-1,-4,-3,-3,4,1,-1,-4],
           'C':[0,-3,-3,-3,9,-3,-4,-3,-3,-1,-1,-3,-1,-2,-3,-1,-1,-2,-2,-1,-3,-3,-2,-4],'Q':[-1,1,0,0,-3,5,2,-2,0,-3,-2,1,0,-3,-1,0,-1,-2,-1,-2,0,3,-1,-4],
           'E':[-1,0,0,2,-4,2,5,-2,0,-3,-3,1,-2,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],'G':[0,-2,0,-1,-3,-2,-2,6,-2,-4,-4,-2,-3,-3,-2,0,-2,-2,-3,-3,-1,-2,-1,-4],
           'H':[-2,0,1,-1,-3,0,0,-2,8,-3,-3,-1,-2,-1,-2,-1,-2,-2,2,-3,0,0,-1,-4],'I':[-1,-3,-3,-3,-1,-3,-3,-4,-3,4,2,-3,1,0,-3,-2,-1,-3,-1,3,-3,-3,-1,-4],
           'L':[-1,-2,-3,-4,-1,-2,-3,-4,-3,2,4,-2,2,0,-3,-2,-1,-2,-1,1,-4,-3,-1,-4],'K':[-1,2,0,-1,-3,1,1,-2,-1,-3,-2,5,-1,-3,-1,0,-1,-3,-2,-2,0,1,-1,-4],
           'M':[-1,-1,-2,-3,-1,0,-2,-3,-2,1,2,-1,5,0,-2,-1,-1,-1,-1,1,-3,-1,-1,-4],'F':[-2,-3,-3,-3,-2,-3,-3,-3,-1,0,0,-3,0,6,-4,-2,-2,1,3,-1,-3,-3,-1,-4],
           'P':[-1,-2,-2,-1,-3,-1,-1,-2,-2,-3,-3,-1,-2,-4,7,-1,-1,-4,-3,-2,-2,-1,-2,-4],'S':[1,-1,1,0,-1,0,0,0,-1,-2,-2,0,-1,-2,-1,4,1,-3,-2,-2,0,0,0,-4],
           'T':[0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,1,5,-2,-2,0,-1,-1,0,-4],'W':[-3,-3,-4,-4,-2,-2,-3,-2,-2,-3,-2,-3,-1,1,-4,-3,-2,11,2,-3,-4,-3,-2,-4],
           'Y':[-2,-2,-2,-3,-2,-1,-2,-3,2,-1,-1,-2,-1,3,-3,-2,-2,2,7,-1,-3,-2,-1,-4],'V':[0,-3,-3,-3,-1,-2,-2,-3,-3,3,1,-2,1,-1,-2,-2,0,-3,-1,4,-3,-2,-1,-4],
           'B':[-2,-1,3,4,-3,0,1,-1,0,-3,-4,0,-3,-3,-2,0,-1,-4,-3,-3,4,1,-1,-4],'Z':[-1,0,0,1,-3,3,4,-2,0,-3,-3,1,-1,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],
           'X':[0,-1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,0,0,-2,-1,-1,-1,-1,-1,-4],'*':[-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,1]}
# Read BLOSUM and write them in a dictionary.
BLOSUM = pd.DataFrame(BLOSUM, columns = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*'],
                       index = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*'])
# This step is intended to be translated into a form that is easier for people to understand. My classmate taught me this operation.
print(BLOSUM)
total_score1 = 0
for n in range(len(file1)):
    score1 = BLOSUM.loc[file1[n],file2[n]]# We use the BLOSM to score the alignment in human and mouse DLX5 sequence.
    total_score1 = total_score1 + score1
print("The score for alignment in human and mouse DLX5 sequence is:", total_score1)
# The latter steps are similar to the ideas in this section.
total_score2 = 0
for n in range(len(file1)):
    score2 = BLOSUM.loc[file1[n],file3[n]]# Similar to the previous step
    total_score2 = total_score2 + score2
print("The score for alignment in human DLX5 and random sequence is:", total_score2)
total_score3 = 0
for n in range(len(file2)):
    score3 = BLOSUM.loc[file2[n],file3[n]]
    total_score3 = total_score3 + score3
print("The score for alignment in mouse DLX5 and random sequence is:", total_score2)
similarity1 = 0
for n in range(len(file1)):
    if file1[n] == file2[n]:
        similarity1 += 1
percentage1 = similarity1/len(file1)
#calculate the percentage of the similarity between human and mouse DLX5 sequence
print("The percentage of identical amino acids for the comparison between human and mouse DLX5 sequence is", percentage1)
similarity2 = 0
for i in range(len(file1)):
    if file1[i] == file3[i]:
        similarity2 += 1
percentage2 = similarity2/len(file1)
#These codes are used to calculate the percentage of the similarity between human DLX5 and random sequence.
print("The percentage of identical amino acids for the comparison between human DLX5 and random sequence is", percentage2)
similarity3 = 0
for n in range(len(file2)):
    if file2[n] == file3[n]:
        similarity3 += 1
percentage3 = similarity3/len(file2)
#The percentage of the similarity between mouse DLX5 and random sequence
print("The percentage of identical amino acids for the comparison between mouse DLX5 and random sequence is", percentage3)