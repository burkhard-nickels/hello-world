"""
Module server - Network Server
"""
import socket
import sys
from time import sleep
from base.pico import Pico

class Server(Pico):
    """
    Class Server - Network Server with sockets.
    """
    def __init__(self,host,port):
        """
        Server(host,port) - Constructor
        """
        super().__init__()
        # host = socket.gethostname()
        # host = socket.getaddrinfo('lenny', port)
        self.port = port
        self.host = host
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind()

    def bind(self):
        """
        bind() - Bind to Network.
        """
        bound = False
        i = 0
        while not bound:
            bound = True
            try:
                self.server.bind((self.host,self.port))
            except OSError as exception:
                message = str(exception)
                self.debug("Server::bind() Error Bind (%d) %s!" % (i,message))
                if(message == "[Errno 98] EADDRINUSE" and i < 3):
                    bound = False
                else:
                    self.debug("Server::bind() Error Bind (%d) Exit!" % (i))
                    sys.exit()
                i += 1
                sleep(3)
        self.debug("Server::bind() Bound to %s:%d" % (self.host,self.port))

    def listen(self):
        """
        listen() - Listen on Server TCP Port.
        """
        listened = False
        i = 0
        while not listened:
            listened = True
            try:
                self.server.listen(10)
                self.log("Server::listen() Listen to %s:%d" % (self.host, self.port))
            except OSError as exception:
                listened = False
                message = str(exception)
                if message == "[Errno 98] EADDRINUSE" and i == 0:
                    self.debug("Servier::listen() " + message + "!")
                if i<3:
                    listened = False
                else:
                    self.debug("Server::listen() Error Listen (%d) Exit!" % (i))
                    sys.exit()
                i += 1
                sleep(3)

    def accept(self,func):
        """
        accept() - Accept/Wait for client connections.
        """
        conn, address = self.server.accept()
        self.debug("Server::accept() Connection from: " + str(address))
        i = 0
        while True:
            data = conn.recv(1024).decode() # receive data
            data = str(data)
            if not data:
                break
            i += 1
            response = func(data)   # Introduced callback, similar to webserver.
            # self.file(data)       # Write data to file
            # data = 'OK'           # Send back "OK"
            conn.send(response.encode())  # send to the client

        conn.close()

    def file(self,data):
        """
        file(data) - Write data to file.
        """
        timestamp = Pico.timestamp()           # Klassen Methode (Funktion)
        data = timestamp + " " + data
        self.debug("Server::file() %s" % (data))
        fhd = open('pico_data.txt','a')
        fhd.write(data + "\n")
        fhd.close()

    def run(self,func):
        """
        run() - Run Server in endless loop to wait for connections.
        """
        self.listen()
        while True:
            self.accept(func)

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        obj = Server("192.168.2.90",5000)
        obj.bind()
        obj.run(Server.test_func)

    @staticmethod
    def test_func(data):
        """
        test_func() - Callback for test.
        """
        print("TESTFUNC: " + data)
        return "OK"

# -------------------------------------------------------
