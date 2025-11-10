import socket
import json


HOST = "127.0.0.1"
PORT = 65432


def build_json_response():
    """Create a simple JSON object to send to the client"""
    data = {
        "status": "ok",
        "message": "Hello from the JSON server",
        "numbers": [1, 2, 3],
        "active": True
    }
    return data


def main():
    """Server: listen for commands and send JSON"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")

            while True:
                data = conn.recv(1024)
                if not data:
                    break

                command = data.decode("utf-8").strip()
                print(f"Received command: {command}")

                if command == "get json":
                    response_data = build_json_response()
                else:
                    response_data = {
                        "status": "error",
                        "message": "Unknown command"
                    }

                response_text = json.dumps(response_data)
                conn.sendall(response_text.encode("utf-8"))


if __name__ == "__main__":
    main()
