"""
Module Flash - Monitoring of Pico Flash Memory.

    Raspberry Pi Pico: 2MB Flash Memory
    - 1,4 MB Image
    - 0,8 MB FS

    ls -lh rp2-pico-w-20230323-unstable-v1.19.1-992-g38e7b842c.uf2
    -rw-r--r-- 1 chuck chuck 1,4M 23. Mär 19:40
          rp2-pico-w-20230323-unstable-v1.19.1-992-g38e7b842c.uf2

    *** from system import fs,name
    *** fs()
    Fs: Size=868352, Free=806912
    *** os.statvfs(".")
    (4096, 4096, 212, 200, 200, 0, 0, 0, 0, 255)
"""

import os
import math
from collections import namedtuple
from base.device import Device

Values = namedtuple("Values", "size free perc")

class Flash(Device):
    """
    Class Flash - Monitor Pico Flash Memory
    """
    def __init__(self,warn=40,alarm=20):
        """
        Constructor
        """
        super().__init__(warn,alarm)
        self.read()

    def read(self):
        """
        read() - Read values from hardware.
        """
        self.raw  = os.statvfs(".")
        self.size = self.raw[2] * self.raw[1]
        self.free = self.raw[3] * self.raw[1]
        self.perc = (self.free / self.size) * 100
        self.vals = Values(self.size, self.free, self.perc)
        self.value = self.perc
        self.fhem = "Flash: Size=%dBytes, Free=%dBytes, Free=%.1fPcnt" % (self.size,
            self.free,self.perc)

    def html(self, ipaddr=None, port=None):
        """
        html() - Returns HTML.
        """
        value = "(Flash intern 2 MB)<br> Size: %d<br>Free: %d<br>Free: %.1f&percnt;" % (self.size,
            self.free,self.perc)
        if self.perc > self.warn:
            clazz = "green"
        elif self.perc < self.warn:
            clazz = "yellow"
        elif self.perc < self.alarm:
            clazz = "red"
        html = self.html_base(clazz, value)
        return html

    def calculate_steps(self):
        """
        calculate_steps() - Calculates from Percentage the SVG steps for RED.
        """
        value = self.perc
        # Example: Batterie 3,7V Nennspannung, full 3,9V , empty 3,4V.
        vmax = 100 # Config Parameter
        vmin = 0
        vrange = vmax - vmin
        step = vrange / 12
        # self.debug("Flash: %f - %f = %f, step=%f" % (vmax,vmin,vrange,step))
        diff = vmax - value
        stepsf = diff / step
        steps = math.floor(stepsf + 0.5)
        # self.debug("Flash: %f - %f = %f, steps=%f (%d)" % (vmax,value,diff,stepsf,steps))
        return steps

    def svg(self):
        """
        svg() - Returns the SVG for the Flash Memory.
        """
        color_green = "rgb(108,198,74)"
        color_red = "rgb(255,124,174)"
        color = [color_green, color_green, color_green, color_green, color_green, color_green,
            color_green, color_green, color_green, color_green, color_green, color_green]

        steps = self.calculate_steps()
        i = 0
        while i < steps:
            # print(" - %d < %d" % (i,steps))
            color[i] = color_red
            i += 1

        svg = "<svg width=\"90\" height=\"120\" viewbox=\"0 0 120 160\" \n"
        svg += "  xmlns=\"http://www.w3.org/2000/svg\"\n"
        svg += "  xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n"
        svg += "  <rect x=\"20\" y=\"0\" width=\"80\" height=\"10\" \n"
        svg += "    style=\"fill:black;stroke-width:2;stroke:rgb(197,26,74)\" />\n"

        svg += "  <rect x=\"10\" y=\"10\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[11] + ";stroke-width:1;stroke:white\" />\n"
        svg += "  <rect x=\"10\" y=\"22\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[10] + ";stroke-width:1;stroke:white\" />\n"
        svg += "  <rect x=\"10\" y=\"34\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[9] + ";stroke-width:1;stroke:white\" />\n"
        svg += "  <rect x=\"10\" y=\"46\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[8] + ";stroke-width:1;stroke:white\" />\n"
        svg += "  <rect x=\"10\" y=\"58\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[7] + ";stroke-width:1;stroke:white\" />\n"
        svg += "  <rect x=\"10\" y=\"70\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[6] + ";stroke-width:1;stroke:white\" />\n"
        svg += "  <rect x=\"10\" y=\"82\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[5] + ";stroke-width:1;stroke:white\" />\n"
        svg += "  <rect x=\"10\" y=\"94\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[4] + ";stroke-width:1;stroke:white\" />\n"
        svg += "  <rect x=\"10\" y=\"106\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[3] + ";stroke-width:1;stroke:white\" />\n"
        svg += "  <rect x=\"10\" y=\"118\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[2] + ";stroke-width:1;stroke:white\" />\n"
        svg += "  <rect x=\"10\" y=\"130\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[1] + ";stroke-width:1;stroke:white\" />\n"
        svg += "  <rect x=\"10\" y=\"142\" width=\"100\" height=\"12\" \n"
        svg += "    style=\"fill:" + color[0] + ";stroke-width:1;stroke:white\" />\n"

        svg += "  <rect x=\"10\" y=\"10\" width=\"100\" height=\"142\" \n"
        svg += "    fill=\"none\" style=\"stroke-width:2;stroke:grey\" />\n"
        svg += "  <rect x=\"20\" y=\"50\" width=\"80\" height=\"50\" \n"
        svg += "    style=\"fill:lightgrey;stroke-width:4;stroke:green\" />\n"
        svg += "  <text x=\"25\" y=\"90\" fill=\"black\" style=\"font-size:40px;\">HD</text>\n"
        svg += "</svg>\n"
        return svg

    def out(self):
        """
        debug() - Debug.
        """
        debug = ("Block size   : %s" % self.raw[0])
        debug += ("Fragment size: %s" % self.raw[1])
        debug += ("Blocks       : %s" % self.raw[2])
        debug += ("Blocks free  : %s" % self.raw[3])
        debug += ("Blocks avail.: %s" % self.raw[4])
        debug += ("Inodes       : %s" % self.raw[5])
        debug += ("Free Inodes  : %s" % self.raw[6])
        debug += ("Avail Inodes : %s" % self.raw[7])
        debug += ("Mount Flags  : %s" % self.raw[8])
        debug += ("Max Filename Len: %s" % self.raw[9])
        return debug

    @staticmethod
    def fhem_string():
        """
        fhem_string() - Get FHEM String.
        """
        obj = Flash()
        txt = obj.line()
        return ["txt",txt]

    @staticmethod
    def web_string():
        """
        web_string() - Get Web Content String.
        """
        flash = Flash()
        return flash.web()

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        obj = Flash()
        test_vals = obj.get()
        test_fhem = obj.line()
        test_html = obj.html()
        test_debg = obj.out()
        print("Test Free: %f" % test_vals)
        print("Test Fhem: " + test_fhem)
        print("Test Html: " + test_html)
        print("Test Debg: " + test_debg)
