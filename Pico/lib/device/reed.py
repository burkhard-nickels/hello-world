"""
Module device_reed - Control Reed Contact with Pico

   Reed Kontakt und Widerstand
   an GPIO und 3.3V anstecken.
"""
from machine import Pin
from base.device import Device

class Reed(Device):
    """
    Class Reed - Control Reed Contact.
    """
    state = ["CLOSED","OPEN"]

    def __init__(self,source): # Konstruktor
        """
        Reed(source) - Constriuctor wit Pin number.
        """
        super().__init__()
        self.source = source
        self.reed = Pin(source, Pin.IN)
        self.value = 0
        self.read()
        self.fhem = "Reed: Open=%s" % (Reed.state[self.value])

    def read(self):
        """
        read() - Read Reed Contact.
        """
        self.value = self.reed.value()
        return self.value

    # ------------------- Ausgabe Methoden ---------------------

    def html(self,ipaddr=None,port=None):
        """
        html() - Return HTML.
        """
        value = "%d" % (self.value)
        if self.value == 0:
            clazz = "green"
        elif self.value == 1:
            clazz = "red"
        content = Reed.state[self.value] + "(" + value + ")"
        html = self.html_base("reed " + clazz, content)
        return html

    def svg(self):
        """
        svg() - Return SVG.
        """
        if self.value == 1:
            html = self.svg_open()
        elif self.value == 0:
            html = self.svg_closed()
        return html

    def svg_open(self):
        """
        svg_open() - Open Door to present Reed Contact State.
        """
        svg = "<g id=\"door_open_pin" + str(self.source) + "\">\n"
        svg += "<svg width=\"80\" height=\"160\" viewbox=\"0 0 100 250\" \n"
        svg += "  xmlns=\"http://www.w3.org/2000/svg\" \n"
        svg += "  xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n"

        # Türrahmen
        svg += "  <path d=\"M0 0 L0 199 10 199 10 10 90 10 90 199 100 199 100 0 z\" \n"
        svg += "    stroke-width=\"1\" fill=\"rgb(255,124,172)\" stroke=\"black\"/>\n"

        # Türblatt
        svg += "  <rect x=\"12\" y=\"12\" width=\"76\" height=\"187\" \n"
        svg += "    style=\"fill:grey;stroke-width:1;stroke:grey\" />\n"
        svg += "  <path d=\"M12 12 L12 199 60 247 60 60 12 12\" \n"
        svg += "    style=\"fill:lightgrey;stroke-width:1;stroke:rgb(197,26,74)\" />\n"
        svg += "  <path d=\"M17 17 L17 204 M25 25 L25 217 M40 40 L40 227\" \n"
        svg += "    style=\"fill:white;stroke-width:1;stroke:rgb(197,26,74)\" />\n"

        # Türscharniere
        svg += "  <path d=\"M10 50 L46 86 46 96 10 60 z\" \n"
        svg += "    style=\"fill:rgb(127,127,255);stroke-width:1;stroke:rgb(197,26,74)\" />\n"
        svg += "  <path d=\"M10 150 L46 186 46 196 10 160 z\" \n"
        svg += "    style=\"fill:rgb(127,127,255);stroke-width:1;stroke:rgb(197,26,74)\" />\n"
        svg += "</svg>\n</g>\n"
        return svg

    def svg_closed(self):
        """
        svg_closed() - Closed Door to present Reed Contact State.
        """
        svg = "<g id=\"door_closed_pin" + str(self.source) + "\">\n"
        svg += "<svg width=\"80\" height=\"160\" viewbox=\"0 0 100 250\" \n"
        svg += "  xmlns=\"http://www.w3.org/2000/svg\" \n"
        svg += "  xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n"

        # Türrahmen
        svg += "  <path d=\"M0 0 L0 199 10 199 10 10 90 10 90 199 100 199 100 0 z\" \n"
        svg += "    stroke-width=\"1\" fill=\"rgb(255,124,172)\" stroke=\"black\"/>\n"

        # Türblatt
        svg += "  <rect x=\"12\" y=\"12\" width=\"76\" height=\"187\" \n"
        svg += "    style=\"fill:lightgrey;stroke-width:1;stroke:rgb(197,26,74)\" />\n"
        svg += "  <path d=\"M20 12 L20 199 M40 12 L40 199 M60 12 L60 199\" \n"
        svg += "    style=\"fill:white;stroke-width:1;stroke:rgb(197,26,74)\" />\n"

        # Türscharniere
        svg += "  <rect x=\"10\" y=\"50\" width=\"60\" height=\"10\" \n"
        svg += "    style=\"fill:rgb(127,127,255);stroke-width:1;stroke:rgb(197,26,74)\" />\n"
        svg += "  <rect x=\"10\" y=\"150\" width=\"60\" height=\"10\" \n"
        svg += "    style=\"fill:rgb(127,127,255);stroke-width:1;stroke:rgb(197,26,74)\" />\n"
        svg += "</svg>\n</g>\n"
        return svg

    @staticmethod
    def web_string(source):
        """
        web_string() - Get Web Content.
        """
        obj = Reed(source)
        html = obj.web()
        return ["html", html]

    @staticmethod
    def fhem_string(source):
        """
        fhem_string() - Get String for FHEM.
        """
        obj = Reed(source)
        txt = obj.line()
        return ["txt", txt]

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        obj = Reed(0)
        test_vals = obj.get()
        test_fhem = obj.line()
        # test_html = obj.html()
        # test_svg  = obj.svg()
        # test_web  = obj.web()
        if test_vals == 1:
            print("OK  - Test Value: %d" % test_vals)
        else:
            print("NOK - Test Value: %d" % test_vals)
        if test_fhem == "Reed: Open=1":
            print("OK  - Test Fhem: " + test_fhem)
        else:
            print("NOK - Test Fhem: " + test_fhem)
            # print("Test Html: " + test_html)
            # print("Test Svg : " + test_svg)
            # print("Test Web : " + test_web)

# ------------------------------------------------------------
