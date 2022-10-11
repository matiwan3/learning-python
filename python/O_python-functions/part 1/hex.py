# Hexadecimal
# hex()

class CustomHex:
    def __index__(self):
        return 10
    
print(hex(255))
print(hex(1))

c = CustomHex()
print(hex(c))