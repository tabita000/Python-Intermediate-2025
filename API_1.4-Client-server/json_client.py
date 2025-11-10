import socket
import json


HOST = "127.0.0.1"
PORT = 65432


def main():
    """Client: send command and print received JSON"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        command = "get json"
        print(f"Sending command: {command}")
        client_socket.sendall(command.encode("utf-8"))

        data = client_socket.recv(4096)
        json_text = data.decode("utf-8")

        json_data = json.loads(json_text)
        print("Received JSON from server:")
        print(json_data)


if __name__ == "__main__":
    main()
