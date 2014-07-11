#!/usr/bin/env python

import socket
from time import sleep

MSG_LENGTH = 1024

class Socket_Server(object):
    def __init__(self, ipaddr, port, backlog = 20):
        self.ipaddr = ipaddr
        self.port = port
        self.backlog = backlog

        # Start Listening
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind( (ipaddr, port) )
        self.sock.listen(backlog)

    def socket_register(self):
        pass

    def wait_msg(self):
        self.connection = None
        self.cli_addr = None

        while True:
            self.connection, self.cli_addr = self.sock.accept()
            print 'Server connected by', self.cli_addr
            while True:
                msg = self.connection.recv(MSG_LENGTH)
                if not msg:
                    break 
                return msg

    def echo_back(self,msg):
        self.connection.send(msg)

    def close_sock(self):
        self.connection.close()
        self.connection = None
        self.cli_addr = None


class Socket_Client(object):
    def __init__(self, ipaddr, port):
        self.ipaddr = ipaddr
        self.port = port

        # Connect to server
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect( (self.ipaddr, self.port) )

    def send_msg(self, msg):
        self.sock.send(msg)

    def send_recv_msg(self, msg):
        self.sock.send(msg)
        sleep(2)
        buf = self.sock.recv(MSG_LENGTH)
        return buf

    def close_sock(self):
        self.sock.close()

        self.ipaddr = ipaddr
        self.port = port

def test_main():
    role_msg = ''' Please enter the role type:
  1)   Server
  2)   Client
  Q|q) Quit
'''
    while True:
        socket_role = raw_input(role_msg)

        if socket_role == "1":
            print "Starting Server..."
            TEST_IPADDR = 'localhost'
            TEST_PORT = 10010

            server = Socket_Server(TEST_IPADDR, TEST_PORT)
            while True:
                msg = server.wait_msg()
                print msg
            break

        elif socket_role == "2":
            print "Starting Client..."
            TEST_IPADDR = 'localhost'
            TEST_PORT = 10010

            client = Socket_Client(TEST_IPADDR, TEST_PORT)

            client.send_msg("hello server")
            client.close_sock()
            break
        elif socket_role == "Q" or socket_role == "q":
            print "OK. Quit testing."
            return True
        else:
            print "Wrong input!!! Please try again.\n"

if __name__ == "__main__":
    test_main()
