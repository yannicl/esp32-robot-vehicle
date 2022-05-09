import socket

class Radio:

    localIP     = "0.0.0.0"
    broadcoastIP = "255.255.255.255"
    UDP_LOCAL_PORT   = 20935

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message):
        self.socket.sendto(message, (self.broadcoastIP, self.UDP_LOCAL_PORT))
