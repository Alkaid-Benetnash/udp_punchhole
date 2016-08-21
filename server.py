import socket


class Daemon(object):
    BUF_SIZE = 4096

    def __init__(self, host, port):
        """
        create a udp socket bind to specific address
        :param port:
        :param host:
        """
        self.addr = (host, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self.addr)

    def listen(self):
        """
        listen, tell any sender their address.
        :return:
        """
        try:
            print("Listening {}:{}".format(*self.addr))
            while True:
                data, addr = self.socket.recvfrom(self.BUF_SIZE)
                print("Receive message from {}:{}".format(*addr))
                self.socket.sendto("{}:{}".format(*addr).encode(), addr)
                
        except KeyboardInterrupt:
            self.socket.close()
            print("Quit")
