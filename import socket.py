import socket

target = input("Enter the IP address to scan: ")
port_range = input("Enter the range of ports to scan (e.g. 5-500): ")

low_port = int(port_range.split('-')[0])
high_port = int(port_range.split('-')[1])

print("Scanning target", target, "from port", low_port, "to port", high_port)

for port in range(low_port, high_port+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()