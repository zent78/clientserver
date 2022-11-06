import time
import socket
import threading

HEADER = 64
port = 5051

server = "localhost"
print(server)
ADDR =  (server, port)
FORMAT = 'utf-8'
Disconnect_msg = "!DISCONNECT"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(ADDR)
# global addr

def handle_client(conn, addr):
    print (f"[NEW CONNECTION] {addr} connected")
    connected = True
    conn.sendall(b"Welcome to the server!")
    while connected:
        #msg_lengt = conn.recv(HEADER).decode(FORMAT)
        #msg_length = len(msg_length)
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg:
            print(f"[{addr}] {msg!r}")
        if msg == Disconnect_msg:
            connected = False

def start(the_socket):
    the_socket.listen()
    while True:
        conn, addr = the_socket.accept()
        thread = threading.Thread (target=handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start(sock)
