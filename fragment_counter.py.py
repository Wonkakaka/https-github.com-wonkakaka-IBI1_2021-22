import re # Importing a Library
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'# create a string variable seq
Find = re.findall(r'GAATTC',seq)
print("the total number of fragments=",len(Find)+1)