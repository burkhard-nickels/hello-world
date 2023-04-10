"""
Temp - Temperature from Pico
"""

from machine import ADC
from base.device import Device

class Temp(Device):
    """
    Class Temp - Temperature from Pico
    """
    conversion_factor = 3.3 / (65535)

    def __init__(self, warn=28, alarm=35): # Konstruktor
        """
        Constructor
        """
        super().__init__()
        self.warn = warn
        self.alarm = alarm
        self.sensor = ADC(4)
        self.temp10 = 0
        self.read()
        self.fhem = "Temp: Temperature=%.4fGrad" % (self.value)

    def read(self):
        """
        temp = read() - Reads the value from sensor and calculates the temperature.
        """
        value = self.sensor.read_u16()
        volt = value * self.__class__.conversion_factor
        self.value = 27 - (volt - 0.706) / 0.001721
        return self.value

    def html(self,ipaddr=None,port=None):
        """
        html() - Returns HTML for temperature.
        """
        self.read()
        value = "%.2fGrad" % (self.value)
        if self.value < self.warn:
            clazz = "green"
        elif self.value > self.warn:
            clazz = "yellow"
        elif self.value > self.alarm:
            clazz = "red"
        html = self.html_base("temp " + clazz, value)
        return html

    def read10(self):
        """
        read10() - Does 10 measurements and calculates average.
        """
        for _ in range(10):
            temp = self.read()
            summe += temp
        self.temp10 = summe / 10
        return self.temp10

    def calculate_graph(self):
        """
        calculate_graph() - Calculates the adjustment for the thermometer graph.
        """
        temp = self.value
        diff = (temp - 15) * 4    # i.e. (27-15) * 4 = 48
        white = 100 - int(diff)        # i.e. 100 - 48 = 52
        y_value = 40 + white
        height = diff
        return (y_value,height)

        # rect von 40 bis 140 (100)
        # 1 Grad = 4 pixel
        # Range von 20 - 40 Grap = 20 = 80 pixel
        #   d.h 20 pixel frei (unter 20 Grad) ist eine Range von 5 Grad.
        #   d.h 15 Grad muessen abgezogen werden.
        # svg += "  <rect x=\"23\" y=\"40\" width=\"4\" height=\"100\" \n"

    def svg(self):
        """
        svg() - Creates SVG for thermometer
        """
        (y_value,height) = self.calculate_graph()
        self.debug("svg() Calculation temp=%f, y=%d, height=%d" % (self.value,y_value,height))

        svg = "<svg width=\"100\" height=\"170\" viewbox=\"0 0 100 170\"\n"
        svg += "  xmlns=\"http://www.w3.org/2000/svg\"\n"
        svg += "  xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n"
        svg += "  <path d=\"\n"
        svg += "    M20 20 \n"
        svg += "    a10,10 0 0,1 10 10 \n"
        svg += "    l 0 120 -10 0 0 -120 z\"\n"
        svg += "    stroke-width=\"6\" fill=\"white\" stroke=\"lightgrey\"/>\n"
        svg += "  <circle cx=\"25\" cy=\"150\" r=\"14\" stroke=\"lightgrey\"\n"
        svg += "    stroke-width=\"6\" fill=\"blue\" />\n"
        svg += "  <path d=\"\n"
        svg += "    M27 40 l 22 0 \n"
        svg += "    M27 80 l 22 0 \n"
        svg += "    M27 120 l 22 0\"\n"
        svg += "    stroke-width=\"2\" fill=\"red\" stroke=\"red\"/>\n"
        svg += "  <path d=\"M27 44 l 6 0 \n"
        svg += "    M27 48 l 6 0 \n"
        svg += "    M27 52 l 6 0 \n"
        svg += "    M27 56 l 6 0 \n"
        svg += "    M27 60 l 6 0 \n"
        svg += "    M27 64 l 6 0 \n"
        svg += "    M27 68 l 6 0 \n"
        svg += "    M27 72 l 6 0 \n"
        svg += "    M27 76 l 6 0 \n"
        svg += "    M27 84 l 6 0 \n"
        svg += "    M27 88 l 6 0 \n"
        svg += "    M27 92 l 6 0 \n"
        svg += "    M27 96 l 6 0 \n"
        svg += "    M27 100 l 6 0 \n"
        svg += "    M27 104 l 6 0 \n"
        svg += "    M27 108 l 6 0 \n"
        svg += "    M27 112 l 6 0 \n"
        svg += "    M27 116 l 6 0\"\n"
        svg += "    stroke-width=\"1\" fill=\"red\" stroke=\"grey\"/>\n"
        svg += "  <path d=\"M27 60 l 6 0 \n"
        svg += "    M27 100 l 6 0\"\n"
        svg += "    stroke-width=\"1\" fill=\"red\" stroke=\"red\"/>\n"
        svg += "  <text x=\"40\" y=\"37\" fill=\"black\">40</text>\n"
        svg += "  <text x=\"40\" y=\"77\" fill=\"black\">30</text>\n"
        svg += "  <text x=\"40\" y=\"117\" fill=\"black\">20</text>\n"
        svg += "  <rect x=\"23\" y=\"" + str(y_value) + "\" width=\"4\" \n"
        svg += "    height=\"" + str(height) + "\" \n"
        svg += "    stroke-width=\"1\" fill=\"blue\" stroke=\"blue\"/>\n"
        svg += "</svg>\n"
        return svg

    @staticmethod
    def fhem_string():
        """
        fhem_string() - Get String for FHEM.
        """
        obj = Temp()
        txt = obj.line()
        obj.debug("fhem_string() fhem=" + txt)
        return ["txt", txt]

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        obj = Temp()
        test_get  = obj.get()
        test_fhem = obj.line()
        test_html = obj.html()
        print("Test Get : " + str(test_get))
        print("Test Fhem: " + test_fhem)
        print("Test Html: " + test_html)

# --------------------------------------------------------
