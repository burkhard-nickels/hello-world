"""
Module device_power - Monitoring the battery of the Pico.

The Power of the Battery can be monitored on Pin(29) and ADC(3).
"""
import math
from machine import ADC, Pin
from base.device import Device

class Power(Device):
    """
    Class Power - Monitoring the battery/power of the Pico.
    """
    factor = 3.3 / (65535)

    def __init__(self,warn=3.5,alarm=3.2): # Konstruktor
        """
        Power(warn,alarm) - Constructor
        """
        super().__init__(warn,alarm)
        self.pin = Pin(29, Pin.IN)
        self.sensor = ADC(3)
        self.read()
        self.fhem = "Power: Spannung=%.2fV" % (self.value)

    def read(self):
        """
        read() - Read the raw data from Sensor on ADC(3).
        """
        value = self.sensor.read_u16()
        self.value = value * 3 * self.__class__.factor
        return self.value

    def html(self,ipaddr=None,port=None):
        """
        html() - Get HTML.
        """
        value = "%.2fV" % (self.value)
        if self.value > self.warn:
            clazz = "green"
        elif self.value < self.warn:
            clazz = "yellow"
        elif self.value < self.alarm:
            clazz = "red"
        html = self.html_base("power " + clazz, value)
        return html

    def calculate_steps(self):
        """
        calculate_steps() - Calculate the steps for the SVG Graph.
        """
        value = self.value
        # Example: Batterie 3,7V Nennspannung, full 3,9V , empty 3,4V.
        vmax = 3.9   # Config Parameter
        vmin = 3.4
        vrange = vmax - vmin   # = 3.9 - 3.4 = 0.5
        step = vrange / 7      # = 0.5 / 5 = 0.1
        self.debug("Batterie: %f - %f = %f, step=%f" % (vmax,vmin,vrange,step))
        diff = vmax - value              # 3.9 - 3.53 = 0.37
        stepsf = diff / step
        steps = math.floor(stepsf + 0.5)  # ceil(0.37 / 0.1) = ceil(3.7) = 4
        self.debug("Batterie: %f - %f = %f, steps=%f (%d)" % (vmax,value,diff,stepsf,steps))
        if steps > 6:
            self.error("Too high steps value!")
            return None
        return steps

    def svg(self):
        """
        svg() - Get SVG.
        """
        color_green = "rgb(108,198,74)"
        color_yellow = "yellow"
        color_red = "red"
        color = [color_green, color_green, color_green,
            color_green, color_green, color_green, color_green]

        steps = self.calculate_steps()
        if steps is None:
            return ""

        i = 0
        while i < steps:         # 0,1,2,3
            print(" - %d < %d" % (i,steps))
            color[i] = "white"       # = white
            i += 1
        while i < steps:         # 4
            print(" - %d < %d" % (i,steps))
            color[i] = color_green   # green
            i += 1

        if steps == 5:
            color[5] = color_yellow
            color[6] = color_yellow
        elif steps == 6:
            color[6] = color_red

        svg = "<svg width=\"130\" height=\"40\" xmlns=\"http://www.w3.org/2000/svg\" \n"
        svg += "  xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n"
        svg += "  <rect x=\"10\" y=\"5\" width=\"15\" height=\"30\"\n"
        svg += "    style=\"fill:" + color[6] + ";stroke-width:2;stroke:rgb(197,26,74)\" />\n"
        svg += "  <rect x=\"25\" y=\"5\" width=\"15\" height=\"30\"\n"
        svg += "    style=\"fill:" + color[5] + ";stroke-width:2;stroke:rgb(197,26,74)\" />\n"
        svg += "  <rect x=\"40\" y=\"5\" width=\"15\" height=\"30\"\n"
        svg += "    style=\"fill:" + color[4] + ";stroke-width:2;stroke:rgb(197,26,74)\" />\n"
        svg += "  <rect x=\"55\" y=\"5\" width=\"15\" height=\"30\" \n"
        svg += "    style=\"fill:" + color[3] + ";stroke-width:2;stroke:rgb(197,26,74)\" />\n"
        svg += "  <rect x=\"70\" y=\"5\" width=\"15\" height=\"30\" \n"
        svg += "    style=\"fill:" + color[2] + ";stroke-width:2;stroke:rgb(197,26,74)\" />\n"
        svg += "  <rect x=\"85\" y=\"5\" width=\"15\" height=\"30\" \n"
        svg += "    style=\"fill:" + color[1] + ";stroke-width:2;stroke:rgb(197,26,74)\" />\n"
        svg += "  <rect x=\"100\" y=\"5\" width=\"15\" height=\"30\" \n"
        svg += "    style=\"fill:" + color[0] + ";stroke-width:2;stroke:rgb(197,26,74)\" />\n"
        svg += "  <rect x=\"115\" y=\"12\" width=\"5\" height=\"15\" \n"
        svg += "    style=\"fill:black;stroke-width:2;stroke:rgb(197,26,74)\" />\n"
        svg += "</svg>\n"
        return svg

    @staticmethod
    def web_string():
        """
        web_string() - Get Web Content.
        """
        obj = Power()
        return obj.web()

    @staticmethod
    def fhem_string():
        """
        fhem_string() - Get String for FHEM.
        """
        obj = Power()
        txt = obj.line()
        obj.debug("fhem_string() fhem=" + txt)
        return ["txt", txt]

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        obj = Power(0)
        test_fhem = obj.line()
        if test_fhem == "Power: Spannung=0.00V":
            print("OK  - Test Fhem: " + test_fhem)
        else:
            print("NOK - Test Fhem: " + test_fhem)

# -----------------------------------------------------------
