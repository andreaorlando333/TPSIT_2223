# Server per la ricezione dei messaggi
from socket import socket
from socket import AF_INET, SOCK_DGRAM
from socket import SOL_SOCKET, SO_BROADCAST

BUFFER_SIZE = 1024
mystr = "test" #str
#bytes

HOST = "0.0.0.0" # riceve da ovunque
PORT = 5000 # > 1024, già occupate
# possibilità:
# localhost 127.0.0.1 > solo locale
# interfaccia (192.168.95.XXX)

def chatServer():
    print("Server in ascolto...")

    with socket(AF_INET, SOCK_DGRAM) as s:
             s.bind((HOST, PORT))
    while True:
      
            s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
            msg = s.recvfrom(BUFFER_SIZE)
            msg = msg[0].decode('utf8')

            print(msg)



if __name__ == "__main__":
    chatServer()
