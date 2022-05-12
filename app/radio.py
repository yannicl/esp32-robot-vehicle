import socket

class Radio:

    localIP     = "0.0.0.0"
    broadcoastIP = "255.255.255.255"
    UDP_LOCAL_PORT   = 20935

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.localIP, self.UDP_LOCAL_PORT))

    def read(self):
        data,addr = self.socket.recvfrom(1024)
        return data

    def send(self, message):
        self.socket.sendto(message, (self.broadcoastIP, self.UDP_LOCAL_PORT))
