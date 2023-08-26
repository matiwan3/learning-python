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
        
class NumberAlgo():
    def __init__(self, my_array):
        if not isinstance(my_array, list):
            raise TypeError("my_array must be list")
        
        self.my_array = my_array
        
    def max(self):
        max_num = float('-inf')
        for x in range(len(self.my_array)):
            if self.my_array[x] >= max_num:
                max_num = self.my_array[x]
        return max_num
    
    def min(self):
        min_num = float('inf')
        for x in range(len(self.my_array)):
            if self.my_array[x] <= min_num:
                min_num = self.my_array[x]
        return min_num
    
    def avg(self):
        sum = 0
        for x in range(len(self.my_array)):
            sum += self.my_array[x]
        avg = sum / len(self.my_array)
        return round(avg, 3)
    
    def med(self):
        sorted_arr = sorted(self.my_array)
        med = sorted_arr[(len(sorted_arr) - 1)//2]
        return med
        
    
class CarInfo():
    def __init__(self, base_price, mileage, prod_year, still_factor):
        self.base_price = base_price
        self.mileage = mileage
        self.prod_year = prod_year
        self.other_factors = still_factor
        
    def PriceNow(self):
        actual_price = self.base_price - ((2023-self.prod_year) self.mileage self.still_factor)
        
        
        
        
        
        
        
        
        
        