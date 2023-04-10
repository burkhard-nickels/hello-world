"""
Module led

    Klasse Led:
    - Led(source)
    - on()
    - off()

    Example:

    led  = Led(13)     # Use GPIO Pin 13
    ledi = Led('LED')  # Use internal Led
    led.on()
    led.off()
    print(led.get())
    del led
"""

from machine import Pin
from base.device import Device
# we have folder "lib.device" and file "base.device"
# so I think we need a full name.

class Led(Device):
    """
    Class Led - Control LED on Pico.
    """
    number = 0
    led_status = ["Off","On"]

    def __init__(self, source): # Konstruktor
        """
        Constructor - Initializes Pico Pin for LED.
        """
        super().__init__()
        self.source = source
        self.__class__.number += 1
        self.led = Pin(source, Pin.OUT)
        self.off()

    def __del__(self):  # Destruktor does not work, number is not decreased.
        """
        Destructor - to decrease number of controlled LEDs.
        """
        self.__class__.number -= 1

    def destroy(self):  # destroy() works
        """
        destroy() - Because the Destructor does not work a destroy() method was created.
        """
        self.__del__()

    def on(self):
        """
        on() - Switch LED On.
        """
        self.led.on()
        self.value = 1

    def off(self):
        """
        off() - Switch LED Off.
        """
        self.led.off()
        self.value = 0

    def toggle(self):
        """
        toggle() - Toggle LED.
        """
        if self.value == 0:
            self.led.on()
            self.value = 1
        elif self.value == 1:
            self.led.off()
            self.value = 0

    def line(self):
        """
        line() - Returns FHEM data.
        """
        return "Led: %s" % self.__class__.led_status[self.value]

    def html(self,ipaddr=None,port=None):
        """
        html() - Return HTML for Buttons to control LEDs
        """
        if ipaddr is None or port is None:
            return ""

        html_btn = "<h4 class=Led> Led </h4>"
        for btn in ("on","off","toggle"):
            html_btn += "<button onclick=\"window.location.href="
            html_btn += "'http://" + ipaddr + ":" + str(port) + "/web/led/" + btn + "';\"> "
            html_btn += btn + " </button>&nbsp;&nbsp;"
        html = self.html_base("led", html_btn)
        return html

    def svg(self):
        """
        svg(color) - Return SVG Icon for LED.
        """
        if self.value == 0:
            color = "grey"
        elif self.value == 1:
            color = "yellow"
        svg = "<svg width=\"100\" height=\"100\" viewbox=\"0 0 100 100\"\n"
        svg += "  xmlns=\"http://www.w3.org/2000/svg\"\n"
        svg += "  xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n"
        svg += "  <circle cx=\"50\" cy=\"50\" r=\"40\" stroke=\"green\"\n"
        svg += "    stroke-width=\"4\" fill=\"" + color + "\" />\n"
        svg += "  <text x=\"20\" y=\"55\" fill=\"black\" style=\"font-size:14px;\">"
        svg += "    Pin(" + str(self.source) + ")</text>"
        svg += "</svg>\n"
        return svg

# --------------- Static Methods ---------------

    @staticmethod
    def cmd_led_on():
        """
        cmd_led_on() - Led On.
        """
        obj = Led('LED')
        obj.on()

    @staticmethod
    def cmd_led_off():
        """
        cmd_led_off() - Led Off.
        """
        obj = Led('LED')
        obj.off()

    @staticmethod
    def cmd_led_toggle():
        """
        cmd_led_toggle() - Led Toggle.
        """
        obj = Led('LED')
        obj.toggle()

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        obj = Led('LED')
        test_val = obj.get()
        obj.on()
        obj.off()
        obj.toggle()
        test_fhem = obj.line()
        test_html = obj.html("192.168.2.77", 5000)
        test_web  = obj.web("192.168.2.77",5000)
        test_svg  = obj.svg()
        if test_val == 0:
            print("OK  - Test Vals: %d" % test_val)
        else:
            print("NOK - Test Vals: %d" % test_val)
        if test_fhem == "Led: On":
            print("OK  - Test Fhem: " + test_fhem)
        else:
            print("NOK - Test Fhem: " + test_fhem)
        if "href='http://192.168.2.77:5000/web/led/on'" in test_html:
            print("OK  - Test Html: ")
        else:
            print("NOK - Test Html: ")
        if "href='http://192.168.2.77:5000/web/led/on'" in test_web:
            print("OK  - Test Web : ")
        else:
            print("NOK - Test Web : ")
        if "Pin(LED)</text></svg>" in test_svg:
            print("OK  - Test SVG : ")
        else:
            print("NOK - Test SVG : ")

# ------------------------------------------------------------
