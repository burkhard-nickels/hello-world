
import socket
import errno

class Client():

  def __init__(self):
    self.port = 5000
    self.host = '192.168.2.90'
	# self.host = getaddrinfo('lenny', port)[0][-1]

  def connect(self):
    self.client = socket.socket()
    self.client.connect((self.host, self.port))      # connect to the server
    # print("ERROR: Client Connection Error! errno=" + str(errno.errorcode))

  def send(self,data):
      if(self.client):
        raw = data.encode()
        if(len(raw) > 0):
          try:
            self.client.send(raw)        # send 
          except OSError as err:
            print("ERROR: Client send! errno=" + str(errno.errorcode))
        data = self.client.recv(1024).decode() # receive

  def disconnect(self):
    self.client.close()                    # close connection

