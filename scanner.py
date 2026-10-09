import socket
import sys


def scan_ports(host, ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout for the connection attempt
    result = sock.connect_ex((host, ports))
    sock.close()
    if result == 0:
        return True  # Port is open
    else:
        return False  # Port is closed or filtered 

if len(sys.argv) != 4 :
    print ("Usage: python scanner.py <target> <start_port> <end_port>")
    sys.exit(1)

target = sys.argv[1]  # Get the target host from command line arguments
start_port = int(sys.argv[2])  # Get the starting port from command line arguments
end_port = int(sys.argv[3])  # Get the ending port from command line arguments

for port in range(start_port, end_port + 1):
    scan_ports(target, port)
    if scan_ports(target, port):
        print(f"[+] Port {port} is open")
    else:
        print(f"[-] Port {port} is closed")
