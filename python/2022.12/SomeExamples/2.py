# Print the top half of the pattern
for i in range(1, 6):
    # Print the spaces
    for j in range(1, 6-i):
        print(" ", end="")
    
    # Print the first half of the row
    for j in range(1, i+1):
        print(j, end="")
    
    # Print the second half of the row
    for j in range(i-1, 0, -1):
        print(j, end="")
    
    # Move to the next line
    print()

# Print the bottom half of the pattern
for i in range(4, 0, -1):
    # Print the spaces
    for j in range(1, 6-i):
        print(" ", end="")
    
    # Print the first half of the row
    for j in range(1, i+1):
        print(j, end="")
    
    # Print the second half of the row
    for j in range(i-1, 0, -1):
        print(j, end="")
    
    # Move to the next line
    print()