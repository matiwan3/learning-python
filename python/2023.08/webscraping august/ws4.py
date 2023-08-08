# ctrl + shift + P : opens list of options
import socket

def additions(a,b):
    return a + b

def ip_address():
    try:
        # Create a socket object to get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip_address = s.getsockname()[0]
        s.close()
        return local_ip_address
    except Exception as e:
        print("Error while getting the local IP address:", e)
        return None
    
def myUpper(anyword):
    return str(anyword).upper()
# print(ip_address())

class gameCharacter():
    def __init__(self, health, ability_power, strength, traits):
        if not isinstance(health, int) or not isinstance(ability_power, int) or not isinstance(strength, int):
            raise TypeError("health, ability_power and strength must be integers")
        if not isinstance(traits, (str, tuple, list)):
            raise TypeError("traits must be a string, tuple, or list")
        
        self.health = health
        self.ability_power = ability_power
        self.strength = strength
        self.traits = traits
        
        
        
        
        
        
        
        
        
        
        
        
        
        