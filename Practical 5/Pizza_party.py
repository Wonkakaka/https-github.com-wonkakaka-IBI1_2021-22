# Set the maximum number of pieces required
number=64
# The value of n at the beginning
n=1
p=2
# Ensure that the program does not stop until p reaches 64.
while p<number:
        p=(n*n+n+2)/2
        print("when the pieces of pizza is:",p,"the number of cuts is:",n)
        n+=1

