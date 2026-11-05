import socket
import sys

def scan_target(target, ports):
    print(f"Scanning target: {target}")
    print("-----------------------------------")
    
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            s.close()
        except KeyboardInterrupt:
            print("\nExiting script.")
            sys.exit()
        except socket.gaierror:
            print("\nHostname could not be resolved.")
            sys.exit()
        except socket.error:
            print("\nCould not connect to server.")
            sys.exit()

if __name__ == "__main__":
    target_ip = "127.0.0.1"
    target_ports = [21, 22, 80, 443, 3306, 8080]
    scan_target(target_ip, target_ports)