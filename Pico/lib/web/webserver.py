"""
Module webserver - Webserver
"""
import re
from http import Http
from server import Server

class Webserver(Server):
    """
    Class Webserver - Creates a Webserver.
    """
    def __init__(self,host,port):
        """
        Webserver(host,port) - Constructor
        """
        super().__init__(host,port)
        self.count = 0

    def accept(self,func):
        """
        accept(func) - Accepts a connection and calls method "func".
        """
        try:
            while True:
                conn, address = self.server.accept()
                self.debug("accept() Connection from: " + str(address))
                request = conn.recv(1024).decode()
                request = str(request)
                path = Webserver.extract_path(request)
                self.log("accept() Request path=" + str(path))
                if not path:
                    break
                (title,response) = func(path)
                length = len(response)
                self.log("accept() Send Response len=%d" % (length))
                if not request:
                    break
                if title in ("css", "svg", "png"):
                    conn.send(Http.response_header(title))
                    self.send_file(conn,response)
                    self.debug("accept() " + title + " sent")
                elif title == "txt":
                    conn.send(Http.response_header(title))
                    conn.send(response)
                    self.debug("accept() " + title + " sent")
                elif title == "error":
                    conn.send(Http.response_header("NotFound"))
                    conn.send(response)
                    self.debug('accept() NotFound sent')
                else:
                    try:
                        conn.send(Http.response_header("html"))
                        ret1 = conn.send(response.encode())
                        self.log("accept() Send Returncode ret=" + str(ret1))
                        if ret1 < length:
                            rest = response[ret1:]
                            length1 = len(rest)
                            self.log("accept() Send Response len=%d" % (length1))
                            ret2 = conn.send(rest.encode())
                            self.log("accept() Send returncode ret=" + str(ret2))
                    except OSError as exception:
                        self.error("accept() Send Error " + str(exception))
                    self.debug('accept() html sent')
                conn.close()
                self.debug('accept() Connection closed')
        except OSError as exception:
            conn.close()
            self.debug('accept() Connection closed ' + str(exception))

    @staticmethod
    def extract_path(request):
        """
        extract_path(request) - Extract Path from Http Request
        """
        re_comp = re.compile(r"GET (\S+) HTTP")
        match = re_comp.search(request)
        if match:
            path = match.group(1)
        else:
            path = False
        return path

    def send_file(self, conn, filename):
        """
        send_file(conn,filename) - Sends the content of a file to the client.
        """
        self.debug("Send file " + filename)
        fhd = open(filename,'r')
        data = fhd.read(1024)
        while data:
            conn.send(data.encode())
            data = fhd.read(1024)
        fhd.close()

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        obj = Webserver("192.168.2.90",5000)
        obj.bind()
        obj.run(Webserver.test_func)

    @staticmethod
    def test_func(data):
        """
        test_func() - Callback for test.
        """
        print("TESTFUNC: " + data)
        return ("txt","OK")

# --------------------------------------------------------------------------
