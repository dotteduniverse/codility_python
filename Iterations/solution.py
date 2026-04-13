'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros 
that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 
and one of length 3. The number 20 has binary representation 10100 and contains one binary gap 
of length 1. The number 15 has binary representation 1111 and has no binary gaps. 
The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary 
representation 10000010001 and so its longest binary gap is of length 5. 
Given N = 32 the function should return 0, because N has binary representation '100000' 
and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].'''
def solution(N):
    # Convert the number to binary and remove the '0b' prefix
    binary_representation = bin(N)[2:] # Get the binary representation of N and remove the '0b' prefix

    max_gap = 0 # Initialize the maximum gap length
    current_gap = 0 # Initialize the current gap length
    in_gap = False # Flag to indicate if we are currently in a gap

    for digit in binary_representation:
        if digit == '1': # If we encounter a '1', we check if we were in a gap
            if in_gap:# If we were in a gap, we compare the current gap length with the maximum gap length and update it if necessary
                max_gap = max(max_gap, current_gap) # Update the maximum gap length if the current gap is longer
                current_gap = 0 # Reset the current gap length for the next potential gap
            in_gap = True # Set the flag to indicate that we are now in a gap
        elif in_gap: # If we encounter a '0' and we are currently in a gap, we increment the current gap length
            current_gap += 1 # Increment the current gap length

    return max_gap # Return the maximum gap length found