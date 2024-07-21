import socket
import threading

# Server code
def start_server():
    def handle_client(client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Received: {message}")
                    broadcast(message, client_socket)
                else:
                    break
            except:
                break
        client_socket.close()

    def broadcast(message, client_socket):
        for client in clients:
            if client != client_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    client.close()
                    clients.remove(client)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen()
    clients = []

    print("Server started...")
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"New connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

# Client code
def start_client():
    def receive_messages(client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Received: {message}")
                else:
                    break
            except:
                break
        client_socket.close()

    def send_messages(client_socket):
        while True:
            message = input("Enter message: ")
            client_socket.send(message.encode('utf-8'))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))

    threading.Thread(target=receive_messages, args=(client,)).start()
    threading.Thread(target=send_messages, args=(client,)).start()

# Run server or client based on user input
if __name__ == "__main__":
    role = input("Enter 'server' to start server or 'client' to start client: ").strip().lower()
    if role == 'server':
        start_server()
    elif role == 'client':
        start_client()
    else:
        print("Invalid input. Please enter 'server' or 'client'.")
