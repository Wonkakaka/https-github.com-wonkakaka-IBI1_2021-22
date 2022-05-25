DNA_input = input("Please input a random DNA sequenece:")
import re # import re function
DNA_sequence = ''.join(re.findall(r'[a-zA-Z]', DNA_input))
# Identify DNA sequences in the letters a-z and A-Z and store them in a list called 'DNA_sequences'.This step can handle mixed-case DNA sequences.
A_sequence = re.findall(r'[aA]', DNA_sequence)
# Store all the "A or a"  in the DNA sequence in a list called the A_sequence.
G_sequence = re.findall(r'[gG]', DNA_sequence)
C_sequence = re.findall(r'[cC]', DNA_sequence)
T_sequence = re.findall(r'[tT]', DNA_sequence)
# These three steps have the same intent as the previous one.
def g(x):
    y = x/len(DNA_sequence)
    return y
# We define a new function to calculate the proportion of each part, and name it g(x).
# I used len to calculate the number of four different parts of the DNA sequence.
x = len(A_sequence)
print(g(x), "is the percentage of A+a")
# calculate the percentage of 'A/a'
x = len(G_sequence)
print(g(x), "is the percentage of G+g")
# calculate the percentage of 'G/g'
x = len(C_sequence)
print(g(x), "is the percentage of C+c")
# calculate the percentage of 'C/c'
x = len(T_sequence)
print(g(x), "is the percentage of T+t")
#calculate the percentage of 'T/t'
# For example:
# Input:aTAGCTtaggTc
# Print:0.25 is the percentage of A+a
#       0.25 is the percentage of G+g
#       0.16666666666666666 is the percentage of C+c
#       0.3333333333333333 is the percentage of T+t