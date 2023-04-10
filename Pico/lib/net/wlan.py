"""
Module wlan - WLAN Connection.
"""
import binascii
import machine
import network
from base.pico import Pico

class Wlan(Pico):
    """
    Class Wlan() - Class for Wlan Connection.
    """

    def __init__(self,ssid,key,ipaddr,netw,gateway): # Konstruktor
        """
        Wlan(ssid, key) - Constructor
        """
        super().__init__()
        self.ssid    = ssid
        self.key     = key
        self.ipaddr  = ipaddr
        self.network = netw
        self.gateway = gateway
        self.nic     = network.WLAN(network.STA_IF)
        self.nic.active(True)
        self.debug("Wlan::init() Wlan %s activated." % (self.ssid))

    def isconnected(self):
        """
        isconnected() - Returns if network is connected.
        """
        return self.nic.isconnected()

    def connect_dhcp(self): # Same name with different parameters is not allowed.
        """
        connect_dhcp() - Connects to Wlan and Creates Interface from DHCP.
        """
        self.connect()

    def connect(self):
        """
        connect(ip,net,gw) - Connects to Wlan and creates Network Interface.
        """
        self.debug("connect(): ssid=%s, key=%s" % (self.ssid,self.key))
        self.debug("connect(): nic=%s, type=%s" % (self.nic, type(self.nic)))
        # scan_result = self.nic.scan()
        if not self.nic.isconnected():
            # buffer1 = bytearray(1024)
            password = str(self.key)
            ret = self.nic.connect(self.ssid.encode(), password.encode())
            self.debug("connect() Connect return=%s" % ret)

        # wlan.connect(net.ssid, auth=(net.sec, 'mywifikey'), timeout=5000)
        while not self.nic.isconnected():
            machine.idle() # save power while waiting

        self.debug('Wlan::connect() WLAN connection succeeded!')
        if(self.ipaddr is None and self.network is None and self.gateway is None):
            ife = self.nic.ifconfig()
        else:
            ife = self.nic.ifconfig((self.ipaddr, self.network, self.gateway, '8.8.8.8'))
            # With parameters is does not return the tuple.
        if ife is not None:
            self.debug("Wlan::connect() Interface: ip=" + ife[0] + ", subnet="
                + ife[1] + ", gateway=" + ife[2] + ", dns=" + ife[3])
            self.ipaddr = ife[0]

    def disconnect(self):
        """
        disconnect() - Disconnect Wlan.
        """
        self.nic.disconnect()
        self.debug('Wlan::disconnect() WLAN disconnected!')

    def get_ip(self):
        """
        get_ip() - Get IP Address.
        """
        return self.ipaddr

    def find(self):
        """
        find() - Finds all reachable Wlan's.
        """
        nets = self.nic.scan()
        nets.sort(key=lambda x:x[3],reverse=True)
        i=0
        for wlan in nets:
            i+=1
            print(i,wlan[0].decode(),binascii.hexlify(wlan[1]).decode(),wlan[2],wlan[3],
                self.security(wlan[4]),
                self.hidden(wlan[5]))
            # ssid, bssid, channel, RSSI, security, hidden

    @staticmethod
    def security(number):
        """
        security() - Returns security value as string.
        """
        security = ["open","WEP","WPA_PSK","WPA2_PSK","WPA/WPA2_PSK","unknown"]
        if number <= 4:
            result = security[number]
        else:
            result = security[5] + "(" + str(number) + ")"
        return result

    @staticmethod
    def hidden(number):
        """
        hidden() - Returns hidden value as string.
        """
        visibility = ["visible","hidden","unknown"]
        if number <= 1:
            result = visibility[number]
        else:
            result = visibility[2] + "(" + str(number) + ")"
        return result

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        obj = Wlan("wlan","123","192.186.2.99","255.255.255.0","192.168.2.1")
        obj.connect()

# --------------------------------------------------------------
