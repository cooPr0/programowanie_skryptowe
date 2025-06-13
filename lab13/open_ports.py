import socket
import sys
from datetime import datetime

def scan_port(ip, port):
    try:
        # Tworzenie nowego gniazda
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Ustawienie timeoutu na 1 sekunde
        sock.settimeout(1)
        # Proba polaczenia z portem
        result = sock.connect_ex((ip, port))
        if result == 0:
            # Pobranie nazwy serwisu jesli jest dostepna
            try:
                service = socket.getservbyport(port)
            except:
                service = "nieznany"
            print(f"Port {port} jest otwarty - serwis: {service}")
        sock.close()
    except socket.error:
        print(f"Blad podczas skanowania portu {port}")

def main():
    # Ustawienie celu na localhost
    target = "127.0.0.1"
    
    # Lista popularnych portow do przeskanowania
    common_ports = [
        20,    
        21,    
        22,    
        23,    
        25,    
        53,    
        80,    
        110,   
        143,   
        443,   
        3306,  
        3389,  
        5432,  
        8080,  
        3000  
    ]
    
    print(f"\nRozpoczynam skanowanie portow na {target}")
    
    # Skanowanie wszystkich okreslonych portow
    for port in common_ports:
        print(f"Skanowanie portu {port}")
        scan_port(target, port)
    
    print("\nSkanowanie zakonczone!")

if __name__ == "__main__":
    main()
