# Client per l'invio dei messaggi

from socket import socket
from socket import AF_INET, SOCK_DGRAM
from socket import SOL_SOCKET, SO_BROADCAST
BUFFER_SIZE = 1024
HOST = "192.168.95.255"
PORT = 5000

def chatClient():
    username = input("Inserisci username: ")
    username = username.encode('utf8')
    while True:
        with socket(AF_INET, SOCK_DGRAM) as s:
            s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
            msg = input("Inserisci un messaggio da inviare: ")
            msg = msg.encode('utf8')
            s.sendto(username, (HOST, PORT))
            s.sendto(msg,(HOST, PORT))

if __name__ == "__main__":
    chatClient()
