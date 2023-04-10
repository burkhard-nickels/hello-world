"""
Module config - Configuration of application.
"""
from os import stat
import re

class Config():
    """
    Class Config - Read Configuration.
    """

    def __init__(self,cfg="pico.cfg"):
        """
        Config(cfg) - Constructor with Filename as Parameter.
        """
        self.config = {'config':True}
        if cfg is None:
            self.file = "pico.cfg"
        else:
            self.file = cfg
        self.read()

    def get(self,key):
        """
        get(key) - Get a Value from Config.
        """
        try:
            val = self.config[key]
            return val
        except KeyError as exception:
            print("Error " + str(exception))
            return None

    def getall(self):
        """
        getall() - Get all Config.
        """
        return self.config

    def read(self):
        """
        read() - Read Config from File.
        """
        status = stat(self.file)
        if status is not None:
            fhd = open(self.file,'r')
            data = fhd.read()
            fhd.close()
            self.process_config(data)
        else:
            print("Config file not found!")

    def process_config(self,data):
        """
        config(data) - Store Config.
        """
        lines = data.splitlines()
        for line in lines:
            if not line.startswith(('#')):
                (key,val) = line.split('=')
                ret = Config.verify(val)
                self.config[key] = ret

    @staticmethod
    def verify(val):
        """
        verify(value) - Verify Config Entries.
        """
        p_int = re.compile(r"^\d+$")
        p_bool = re.compile(r"True|False")
        m_int = p_int.match(val)
        m_bool = p_bool.match(val)
        if m_int is not None:
            result = int(val)
        elif m_bool is not None:
            if val == "True":
                result = True
            elif val == "False":
                result = False
        else:
            result = val
        return result

    @staticmethod
    def test():
        """
        test() - Test functionality.
        """
        key = "ssid"
        cfg1 = Config("test/test.cfg")
        cfg2 = Config()
        val  = cfg1.get(key)
        vals = cfg2.getall()
        if val == "<SSID>":
            print("OK  - Config key=" + key + ", val=" + val)
        else:
            print("NOK - Config key=" + key + ", val=" + val)
        if vals[key] == "<SSID>":
            print("OK  - Config All key=" + key + ", val=" + vals[key])
        else:
            print("NOK - Config All key=" + key + ", val=" + vals[key])


# ------------------------------------------------------
