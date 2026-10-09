import socket

def scan_ports(host, ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout for the connection attempt
    result = sock.connect_ex((host, ports))
    sock.close()
    if result == 0:
        return True  # Port is open
    else:
        return False  # Port is closed or filtered

target = input("Enter the target IP :  ")

for port in range (1, 101):
    scan_ports(target, port)
    if scan_ports(target, port):
        print(f"[+] Port {port} is open")
    else:
        print(f"[-] Port {port} is closed")
        