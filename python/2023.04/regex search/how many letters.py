import re
import string

letter_counts = {}
for letter in string.ascii_lowercase:
    letter_counts[letter] = 0

# Open the file and read its contents
with open('plenty of text.txt', 'r') as file:
    contents = file.read().lower()

# Count the occurrences of each letter
for letter in contents:
    if letter in letter_counts:
        letter_counts[letter] += 1

# Print the letter counts
for letter, count in letter_counts.items():
    print(f"counter_{letter} = {count}") 