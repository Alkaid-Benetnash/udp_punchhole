import socket

class Daemon(object):
    BUF_SIZE=4096
    def __init__(self, host='0.0.0.0', port=6789):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def listen(self):
        try:
            print("Listening {}:{}".format(self.host, self.port))
            while True:
                data, addr = self.socket.recvfrom(self.BUF_SIZE)
                print("Receive message from {}:{}".format(*addr))
                self.socket.sendto("{}:{}".format(*addr).encode(), addr)
                
        except KeyboardInterrupt:
            self.socket.close()
            print("Quit")