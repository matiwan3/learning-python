import random
import string

# Generate a random string of length 10
# consisting of numbers between "M" and "W"
random_string = "".join(random.choices(string.digits, k=10))

# Prepend "M" to the beginning of the string
# and append "W" to the end of the string
random_id = "M" + random_string + "W"

# Print the random ID
print(random_id)