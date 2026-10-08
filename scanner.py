import socket

print("Welcome to the port scanner")
target = input("Enter the target IP address: ")
port = int(input("Enter the port number to scan: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)

result = sock.connect_ex((target, port))
if result == 0:
    print(f"Port {port} is open")
else:
    print(f"Port {port} is closed")

sock.close()