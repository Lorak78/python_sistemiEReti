"""
chiedere in input ipv4 e subnet mask
1) creare oggetto ip, stampare se ip è privato, se è di loopback
2) se ip di rete, se ip di rete valido, se lo è allora stampa tutti gli ip
   utilizzabili
"""

import ipaddress

def main():
    ip = ipaddress.ip_address(input("inserisci l'indirizzo ip: "))
    subnetMask = input("inserisci la subnet mask")
    print(ip)
    print(f"ip privato: {ip.is_private}")
    print(f"ip di loopback: {ip.is_loopback}")
    ipRete = ipaddress.ip_network(input(f"{ip}/{subnetMask}"))
    if ip == str(ipRete):
        print("è di rete")
    else:
        print("non e' di rete")


    

if __name__ == "__main__":
    main()