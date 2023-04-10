
STA_IF = 0

class WLAN():

    def __init__(self,para):
        self.para = para

    def active(self,state):
        print("Dummy Network active(): state=" + str(state))
        status = state

    def connect(self,ssid,key):
        print("Dummy Network connect(): ssid=" + ssid + ", key=" + str(key));
        return "Connected"

    def disconnect(self):
        print("Dummy Network disconnect()")

    def isconnected(self):
        print("Dummy Network isconnected():")
        return True

    def ifconfig(self, para=None):
        if para is not None:
            ip  = para[0]
            net = para[1]
            gw  = para[2]
            dns = para[3]
            print("Dummy Network ifconfig(): ip=" + ip + ", net=" + net + ", gw=" + gw)
        else:
            return ["192.168.2.5","255.255.255.0","192.168.2.1","8.8.8.8"]

    def scan(self):
        print("Dummy Network WLAN.scan()")
        return "WLAN Dummy"

    def ifconfig(self):
        print("Dummy Network WLAN.ifconfig()")
        return ["192.168.2.5","255.255.255.0","192.168.2.1","8.8.8.8"]
