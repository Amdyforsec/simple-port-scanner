import socket
import sys


def scan_ports(host, ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout for the connection attempt
    try:
        result = sock.connect_ex((host, ports))
        return result == 0  # Return True if the port is open (result is 0)
    finally:
            sock.close()

def grab_banner(host, port):    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        sock.connect((host, port))
        banner = sock.recv(1024).decode().strip()  # Receive the banner and decode it
        return banner or "No banner received"  # Return the banner or a message if no banner is received
    except Exception as e:
        return f"Error grabbing banner: {e}"
    finally:
        sock.close()

if len(sys.argv) != 4 :
    print ("Usage: python scanner.py <target> <start_port> <end_port>")
    sys.exit(1)

target = sys.argv[1]  # Get the target host from command line arguments

try:
    start_port = int(sys.argv[2])  # Get the starting port from command line arguments
    end_port = int(sys.argv[3])  # Get the ending port from command line arguments
except ValueError:
    print("Error: Start port and end port must be integers.")
    sys.exit(1)

if not 1 <= start_port <= 65365:
    print("Start port must be between 1 and 65365 ")
    sys.exit(1)

if not 1 <= end_port <= 65365:
    print("End port must be between 1 and 65365 ")
    sys.exit(1)

for port in range(start_port, end_port + 1):
    if scan_ports(target, port):

        try:
            service = socket.getservbyport(port)  # Attempt to get the service name for the port
        except OSError:
            service = "Unknown"
        banner = grab_banner(target, port)
        print(f"[+] Port {port} is open - Service: {service} - Banner: {banner}")

