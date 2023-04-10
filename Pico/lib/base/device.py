"""
Module device - Delivers a superclass for all devices on Pico.

Saves some implementation in derive classes. I.e.
 get() does not need to be implemented when most important value is called self.value.
 line() no need to implement when fhem string is created as self.fhem.
 web() no need to implement when html() and/or svg() are implemented.
     In case only one is needed, Device delivers the other with an empty string.
 html() should be implemented, but if not needed delivers an empty string.
 svg() should be implemented, but if not needed delivers an empyt string.

Some html() methods need an ipaddr and port in case a link or a button back to the
  application is used, i.e. LED on as button needs a href back to Pico Webserver.
  So for web() and html() both are used with default value to get same signature
  of an overriden method.

 - __init__(warn, alarm)     - Constructor
 - get()                     - Returns self.value
 - line()                    - Returns self.fhem
 - html(ipaddr, port)        - Abstract
 - html_base(hclass,content) - Should be used from derived class to get same div-Element
 - svg()                     - Abstract or if not implemented.
 - web(ipaddr,port)          - Returns HTML from html() and svg()

"""
from base.pico import Pico

class Device(Pico):
    """
    Class Device - Monitoring Devices on Pico.
    """

    def __init__(self,warn=0,alarm=0): # Konstruktor
        """
        Device(warn,alarm) - Constructor with threshold of warn and alarm.
        """
        super().__init__()
        self.warn = warn
        self.alarm = alarm
        self.fhem = "Fhem:"  # Attribute hides method fhem()
        self.value = 0

    def get(self):
        """
        get() - Get most important value.
        """
        self.debug("get() value=" + str(value))
        return self.value

    def line(self):
        """
        line() - Returns string for Home Automation Server.
        """
        self.debug("line() fhem=" + self.fhem)
        return self.fhem

    def html(self,ipaddr=None,port=None):
        """
        html() - Abstract
        """
        if ipaddr is not None:
            url = ipaddr + ":" + port    # Otherwise "unused argument"
            self.debug("Device::html() url=" + url)
        return ""

    def html_base(self,hclass,content):      # hclass = additional functional class, i.e. "green"
        """
        html() - Sets the HTML class ot object class name and functional class.
          i.e. class="Power green"
        """
        clazz = self.__class__.__name__  # clazz = Object Class
        html = "<div class=\"" + clazz + " " + hclass + "\">\n  " + content + "</div>\n"
        return html

    def svg(self):
        """
        svg() - Abstract
        """
        self.debug("Device::svg()")
        return ""

    def web(self,ipaddr=None,port=None):
        """
        web() - Get HTML for webpage with Status and SVG Graphic.
        """
        html = "<table class=none><tr><td>\n"
        if ipaddr is not None:
            html += self.html(ipaddr,port)
        else:
            html += self.html()
        html += "</td><td>\n"
        html += self.svg()
        html += "</td></tr></table>\n"
        return html

# ---------------------- TEST Methods ---------------------

    @staticmethod
    def test_base(obj):
        """
        test_base() - Method to use in subclasses to ease tests.
        """
        test_val  = obj.get()
        test_fhem = obj.line()
        test_html = obj.html()
        test_svg  = obj.svg()
        test_web  = obj.web()
        if test_val == 0:
            print("OK  - Test Val: " + str(test_val))
        else:
            print("NOK - Test Val: " + str(test_val))
        if test_fhem == "Fhem:":
            print("OK  - Test Fhem: " + test_fhem)
        else:
            print("NOK - Test Fhem: " + test_fhem)
        if test_html == "":
            print("OK  - Test Html: " + test_html)
        else:
            print("NOK - Test Html: " + test_html)
        if test_html == "":
            print("OK  - Test Svg : " + test_svg)
        else:
            print("NOK - Test Svg : " + test_svg)
        if test_web == "<table class=none><tr><td>\n</td><td>\n</td></tr></table>\n":
            print("OK  - Test Web : ")
        else:
            print("NOK - Test Web : ")

    @staticmethod
    def test():
        """
        test() - Function to test/run the functionality.
        """
        obj = Device()
        Device.test_base(obj)

# -----------------------------------------------------------
