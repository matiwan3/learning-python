email = input("Enter Your Email: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username i {username} & domain is {domain}")

#https://github.com/mindninjaX/Python-Projects-for-Beginners/blob/master/Email%20Slicer/Email%20Slicer.py