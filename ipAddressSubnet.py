def main():
    ip_addresses = ["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    subnets = [ip_address[-3:] for ip_address in ip_addresses]
    file = open("mask.txt", "w")
    file.write(f"{subnets}")
    file.close()

def main2():
    ip_addresses = ["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    subnets = [ip_address[-3:] for ip_address in ip_addresses]
    with open("mask.txt", "w") as file:#costrutto with
        file.write(f"{subnets}")

if __name__ == "__main__":
    main()