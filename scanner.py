import socket
from datetime import datetime

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

        sock.close()

    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        exit()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        exit()

    except socket.error:
        print("Could not connect to server.")
        exit()


print("=" * 50)
print("Simple Python Port Scanner")
print("=" * 50)

target = input("Enter target IP or domain: ")

print(f"\nScanning target: {target}")
print(f"Scan started at: {datetime.now()}")
print("-" * 50)

for port in range(1, 1025):
    scan_port(target, port)

print("-" * 50)
print("Scan completed.")