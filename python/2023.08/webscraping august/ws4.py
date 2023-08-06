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
    
# print(ip_address())