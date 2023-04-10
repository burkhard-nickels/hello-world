"""
Main Application
"""

from temp import Temp
from flash import Flash
from system import System, Net, Mem

from base import Config
from base import Pico
from base import Device

from led import Led
from power import Power
from reed import Reed

from wlan import Wlan
from server import Server

class App():
    """
    Class App - Application class
    """

    def __init__(self):
        """
        Constructor - Set sys.path module path.
        """

    @staticmethod
    def run():
        """
        run() - run application.
        """
        # import webserver
        print("Run ...")
        # webserver.run()

    @staticmethod
    def test_system():
        """
        test_system() - Test modules in folder /lib/system/
        """
        print("---------------\nTest Temp ...")
        Temp.test()
        print("---------------\nTest Flash ...")
        Flash.test()
        print("---------------\nTest Name ...")
        Name.test()
        print("---------------\nTest Net ...")
        Net.test()

    @staticmethod
    def test_base():
        """
        test_base() - Test modules in folder /lib/base/
        """
        print("---------------\nTest Config ...")
        Config.test()
        print("---------------\nTest Pico ...")
        Pico.test()
        print("---------------\nTest Device ...")
        Device.test()

    @staticmethod
    def test_device():
        """
        test_device() - Test modules in folder /lib/device/
        """
        print("---------------\nTest Led ...")
        Led.test()
        print("---------------\nTest Power ...")
        Power.test()
        print("---------------\nTest Reed ...")
        Reed.test()

    @staticmethod
    def test_net():
        """
        test_network() - Test modules in folder /lib/network/
        """
        print("---------------\nTest Wlan ...")
        Wlan.test()
        print("---------------\nTest Server ...")
        Server.test()

# ----------------------------------------
