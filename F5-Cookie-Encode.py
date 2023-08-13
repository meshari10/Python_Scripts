import sys

def encode_ip_address(ip_address):
    octets = ip_address.split('.')
    hex_bytes = [hex(int(octet))[2:].zfill(2) for octet in octets]
    reversed_hex = ''.join(hex_bytes[::-1])
    decimal_value = int(reversed_hex, 16)
    return decimal_value

def encode_port(port):
    hex_value = hex(port)[2:].zfill(4)
    reversed_hex = hex_value[2:] + hex_value[:2]
    decimal_value = int(reversed_hex, 16)
    return decimal_value

def encode_persistence_cookie(ip_address, port):
    encoded_ip = encode_ip_address(ip_address)
    encoded_port = encode_port(port)
    persistence_cookie = f"{encoded_ip}.{encoded_port}.0000"
    return persistence_cookie

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python F5-Cookie-Encode.py <IP address> <port>")
        sys.exit(1)

    ip_address = sys.argv[1]
    port = int(sys.argv[2])

    persistence_cookie = encode_persistence_cookie(ip_address, port)
    print(persistence_cookie)
