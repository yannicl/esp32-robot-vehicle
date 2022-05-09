import socket

class Radio:

    localIP     = "0.0.0.0"
    UDP_LOCAL_PORT   = 20935

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message):
        if self.lastClientAddress:
            self.socket.sendto(message, (self.localIP, self.UDP_LOCAL_PORT))


