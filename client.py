import socket


class Client(object):
    BUF_SIZE = 4096
    TIME_OUT = 5

    def __init__(self, host, port):
        """
        create a udp socket, if specific a port, then bind to that address.
        :param host:
        :param port:
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if port is not None:
            if host is None:
                host = ''
            self.socket.bind((host, port))

    def punch(self, remote_addr):
        """
        send a message to a remote_addr,
        :param remote_addr:
        :return:
        """
        self.socket.sendto(b'hello', remote_addr)
        try:
            data, addr = self.socket.recvfrom(self.BUF_SIZE)
            print(data.decode())
        except socket.timeout:
            print("No Response")
