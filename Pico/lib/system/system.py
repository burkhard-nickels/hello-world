"""
Module pico_system - System functions for Pico.
"""

import os
import gc
import sys
import machine
from base.device import Device

class Name(Device):
    """
    Class Name - Gets the Pico System name.

    #  >>> os.uname()
    # (sysname='rp2', nodename='rp2', release='1.19.1',
    #  version='v1.19.1-992-g38e7b842c on 2023-03-23 (GNU 12.1.0 MinSizeRel)',
    #  machine='Raspberry Pi Pico W with RP2040')
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.raw = os.uname()
        self.value = self.raw.sysname
        self.fhem = "Name: "
        self.fhem += "Sysname=%s," % self.raw.sysname
        self.fhem += "Release=%s," % self.raw.release
        self.fhem += "Machine=%s" % self.raw.machine

    def html(self,ipaddr=None,port=None):
        """
        html() - Returns HTML.
        """
        content = "Sysname: %s<br>" % self.raw.sysname
        content += "Release: %s<br>" % self.raw.release
        content += "Machine: %s<br>" % self.raw.machine
        html = self.html_base("name", content)
        return html

    def out(self):
        """
        debug() - Debug detailed osname information.
        """
        debug = ("Sysname : %s" % (self.raw.sysname))
        debug += ("Nodename: %s" % (self.raw.nodename))
        debug += ("Release : %s" % (self.raw.release))
        debug += ("Version : %s" % (self.raw.version))
        debug += ("Machine : %s" % (self.raw.machine))
        return debug

    @staticmethod
    def fhem_string():
        """
        fhem_string() - Get String for FHEM.
        """
        obj = Name()
        txt = obj.line()
        return ["txt", txt]

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        name = Name()
        test_get  = name.get()
        test_fhem = name.line()
        test_html = name.html()
        test_debg = name.out()
        print("Test Get : " + test_get)
        print("Test Fhem: " + test_fhem)
        print("Test Html: " + test_html)
        print("Test Debg: " + test_debg)

# ------------------ ---------------------------

class Net(Device):
    """
    Class Net - Monitor Network Information.

    # >>> network.WLAN()
    # <CYW43 STA down 0.0.0.0>
    # >>> nic = network.WLAN()
    # >>> nic.config('txpower')
    # 31
    # >>> nic.config('mac')
    # b'(\xcd\xc1\t\xe8\xa0'
    # >>> nic.config('hostname')
    # 'PicoW'
    # >>> nic.ifconfig()
    # ('0.0.0.0', '0.0.0.0', '0.0.0.0', '0.0.0.0')
    # >>> nic.status()
    # 0
    # >>> import machine
    # >>> machine.freq()
    # 125000000
    # >>> machine.unique_id()
    # b'\xe6ad\x08C\x81\x96&'
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.value = "TBD"
        self.fhem = "Fhem: TBD"
        print("Not implemented")

    def html(self,ipaddr=None,port=None):
        """
        html() - Get HTML.
        """
        return self.value

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        obj = Net()
        test_vals = obj.get()
        # test_fhem = obj.fhem()
        test_html = obj.html()
        print("Test Free: " + test_vals)
        # print("Test Fhem: " + test_fhem)
        print("Test Html: " + test_html)

# ------------------ Memory ---------------------------

class Mem(Device):
    """
    Class Mem - Monitor Memory Information.
    """

    def __init__(self):
        """
        Mem() - Constructor
        """
        super().__init__()
        self.read()
        self.value = self.perc
        self.fhem = "Memory: Perc=%.2f Mem=%d, Alloc=%d, Free=%d" % (self.value,
            self.mem, self.alloc, self.free)

    def read(self):
        """
        read() - Reads raw data from system.
        """
        self.alloc = gc.mem_alloc()
        self.free  = gc.mem_free()
        self.mem   = self.alloc + self.free
        self.perc  = (self.alloc / self.mem) * 100
        self.raw = [ self.mem, self.alloc, self.free ]

    @staticmethod
    def collect():
        """
        collect() - Do a Garbage Collection
        """
        mem1 = gc.mem_alloc()
        gc.collect()
        mem2 = gc.mem_alloc()
        mem3 = mem1 - mem2
        result = "Garbage Collection: Freed %d Bytes (%d - %d)." % (mem3,mem1,mem2)
        return result

    def html(self,ipaddr=None,port=None):
        """
        html()
        """
        content = "<div class=\"Mem mem\"> (Memory 264 kB RAM)<br>\n"
        content += "  Mem: " + str(self.mem) + "<br>\n"
        content += "  Mem Used: " + str(self.alloc) + "<br>\n"
        content += "  Mem Free: " + str(self.free)
        content += "</div>\n"
        content += "<button onclick=\"window.location.href="
        content += " 'http://" + ipaddr + ":" + str(port) + "/pico/gc';\">"
        content += " GC </button>\n"
        html = self.html_base("mem", content)
        return html

# ------------- Static Methods ------------

    @staticmethod
    def cmd_gc():
        """
        fhem_strin() - Returns the FHEM String.
        """
        Mem.collect()

    @staticmethod
    def fhem_string():
        """
        fhem_strin() - Returns the FHEM String.
        """
        obj = Mem()
        txt = obj.line()
        return ["txt",txt]

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        obj = Mem()
        test_vals = obj.get()
        print("Test " + str(test_vals))

# ------------------ ---------------------------

class System(Device):
    """
    Class System - System Functionality
    """

    def __init__(self):
        """
        System() - Constructor
        """
        super().__init__()
        self.value = 1

    def html(self,ipaddr=None,port=None):
        """
        html()
        """
        content = "  <button onclick=\"window.location.href=\n"
        content += "    'http://" + ipaddr + ":" + str(port) + "/web/shutdown';\">\n"
        content += "     Shutdown Web </button>\n"
        content += "  <button onclick=\"window.location.href=\n"
        content += "    'http://" + ipaddr + ":" + str(port) + "/pico/reset';\">\n"
        content += "    Reset </button>\n"
        content += "  <button onclick=\"window.location.href=\n"
        content += "    'http://" + ipaddr + ":" + str(port) + "/pico/soft_reset';\">\n"
        content += "    Soft Reset </button>\n"
        html = self.html_base("stop", content)
        return html

    @staticmethod
    def cmd_reset():
        """
        cmd_reset() - Resets the Pico
        """
        machine.reset()

    @staticmethod
    def cmd_soft_reset():
        """
        cmd_soft_reset() - Soft resets the Pico.
        """
        machine.soft_reset()

    @staticmethod
    def cmd_exit():
        """
        cmd_exit() - Exit the program.
        """
        sys.exit()

# ------------------ ---------------------------
