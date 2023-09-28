import socket
import sys

def save_hex_data(data):
    with open('received_data.bin', 'ab') as file:
        # file.write(data.hex() + '\n')
        file.write(data)

def calculate_checksum(data):
    checksum = sum(data) & 0xFF
    return checksum.to_bytes(1, byteorder='big')

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Client connected from {client_address[0]}:{client_address[1]}")

        while True:
            data = client_socket.recv(1300)
            if not data:
                break

            save_hex_data(data)
        client_socket.close()
        print("Client disconnected")

        server_socket.close()
        return

if __name__ == '__main__':
    # 指定服务器的主机和端口
    host ='192.168.0.20' # 可替换为服务器的 IP 地址
    port = 8080      # 可替换为任意可用端口号

    start_server(host, port)
    sys.exit()
