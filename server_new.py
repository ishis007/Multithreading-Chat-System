import socket
import threading
import datetime

HOST = '127.0.0.1'
PORT = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}  # name -> socket
lock = threading.Lock()

print("Server started...")

def broadcast(message, exclude=None):
    for name, client in clients.items():
        if name != exclude:
            client.send(message.encode('utf-8'))

def send_user_list():
    users = ",".join(clients.keys())
    broadcast(f"USERS:{users}")

def handle_client(client):
    name = client.recv(1024).decode('utf-8')

    with lock:
        clients[name] = client

    broadcast(f"SYSTEM:{name} joined the chat")
    send_user_list()

    try:
        while True:
            msg = client.recv(1024).decode('utf-8')
            timestamp = datetime.datetime.now().strftime("%H:%M")

            if msg.startswith("@"):
                target, content = msg.split(" ", 1)
                target = target[1:]

                if target in clients:
                    clients[target].send(
                        f"[{timestamp}] (Private) {name}: {content}".encode('utf-8')
                    )
            else:
                broadcast(f"[{timestamp}] {name}: {msg}", exclude=None)

    except:
        pass

    with lock:
        del clients[name]

    broadcast(f"SYSTEM:{name} left the chat")
    send_user_list()
    client.close()

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client,), daemon=True).start()
