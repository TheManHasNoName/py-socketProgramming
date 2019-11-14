from __future__ import print_function
import socket
import sys

#create socket (allows to connect to other computer)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s= socket.socket()
    except socket.error as msg:
        print("Socket error: " + str(msg))

#bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Bind socket to port: " + str(port))
        s.bind((host, port))
        s.listen(10)
    except socket.error as msg:
        print("Socket bind error: " + str(msg) + "\n" + "retrying...")
        socket_bind()

#establish connectino with client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()

#send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            sys.exit()
        if len(str.encode(cmd)) >= 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

if __name__ == '__main__':
    socket_create()
    socket_bind()
    socket_accept()