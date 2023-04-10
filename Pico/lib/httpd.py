"""
Main HTTPD Server Program
"""
from web.html import Html
from wlan import Wlan
from pico import Pico
import pico

# -------- Pico internal system
from temp import Temp
from flash import Flash
from system.system import Name
from system.system import System
from system.system import Mem

# -------- Devices connected to Pico
from reed import Reed
from led import Led
from power import Power

from webserver import Webserver
from config import Config

# - Modulauswahl ueber Config

# --------------- Global Vars ---------------

CFG = None     # Configuration
# pico.DEBUG[0] = True

# ------------------------------------------

class Httpd(Pico):
    """
    Class Httpd - Class for Httpd Server
    """
    def __init__(self):
        super().__init__()
        self.log("Start HTTPD Server ...")

        config = Config(None)        # File pico.cfg is default.
        global CFG                   # globel is necessary to change global cfg.
        CFG = config.getall()        # i.e. cfg["ssid"]

        self.led = Led('LED')
        pico.DEBUG[0] = CFG["debug"]
        self.log("Httpd() - Debug=" + str(pico.DEBUG))
        self.init_route()

    def handler(self,path):
        """
        handler() - Callback function to handle http requests.
        """
        if path:
            self.debug("handler() Path=" + path)
            ret = self.distribute(path)
        else:
            html = Html(CFG["ip"],CFG["port"])
            ret = html.main_error()

        self.debug("handler() return=" + str(ret))
        freed = Mem.collect()
        self.debug(freed)
        self.debug("handler() return=" + str(ret))
        return ret

    def distribute(self,path):
        """
        distribute() - Distributes the Http Path.

        path distribution:
        - Function: Function must return array [type, string],
           i.e. ["txt", <fhem_string>]
           i.e. ["html", <web_string>]
        - Array 2 [type,text]: Direct to Webserver
        - Array 2 [type,func]: Function must return array [type, string],
        - Array 3 [type,func1,func2]: Function2 must return array [type,string]
        """
        try:
            action = self.route[path]
        except KeyError as exception:
            self.error("distribute() Path not available path=" + path + ", " + str(exception))
            html = Html(CFG["ip"],CFG["port"])
            html_error = html.main_error()
            result = ["html",html_error]
            return result

        self.debug("distribute(): " + path)

        action_type = str(type(action))
        self.debug("distribute(): " + action_type)
        if isinstance(action,list):
            action_type0 = str(type(action[0]))
            action_type1 = str(type(action[1]))
            if len(action) == 2 and isinstance(action[1],str):                   # Type and String
                result = action
            elif len(action) == 2 and action_type1 == "<class 'bound_method'>":  # Type and Method
                result = action[1]
            elif len(action) == 2 and action_type1 == "<class 'function'>":      # Type and Function
                result = action[1]
            elif len(action) == 2 and action_type0 == "<class 'function'>":  # Function with Parameter
                result = action[0](action[1])
            elif len(action) == 3:                      # Type and 2 Methods
                action[1]()
                result = action[2]()
        elif action_type == "<class 'bound_method'>":   # Method
            result = action()
        elif action_type == "<class 'function'>":       # Function
            result = action()
        else:
            html = Html(CFG["ip"],CFG["port"])
            html_error = html.main_error()
            result = ["html",html_error]
        return result
        # ============================================

    def webpage(self):
        """
        webpage() - Creates the webpage for Pico.
        """
        content = "<table><tr><td>\n"
        content += Temp().web()
        content += "</td><td>\n"
        content += Reed(CFG["reed"]).web()
        content += "</td><td>\n"
        content += Power.web_string()
        content += "</td></tr>\n"

        content += "<tr><td>\n"
        content += Flash.web_string()
        content += "</td><td>\n"
        timestamp = Pico.timestamp()
        content += Name().html()
        content += "<div class=\"timestamp\">" + timestamp + "</div>\n"
        content += "</td><td>\n"
        content += Mem().web(CFG["ip"],CFG["port"])
        content += "</td></tr>\n"

        content += "<tr><td>\n"
        content += "  <img width=150px src='/kamP.svg'>"
        content += "</td><td>\n"
        content += self.led.web(CFG["ip"],CFG["port"])
        content += "</td><td>\n"
        content += System().web(CFG["ip"],CFG["port"])
        content += "</td></tr></table>\n"

        html = Html(CFG["ip"],CFG["port"])
        main = html.main(CFG["title"],content)
        self.debug("webpage() Html len=" + str(len(main)))
        return ["html",main]

    def start(self):
        """
        start() - Start of Application
        """
        wlan = Wlan(CFG["ssid"],CFG["key"],CFG["ip"],CFG["net"],CFG["gw"])
        wlan.connect()

        message = "Main Start Webserver on %s:%d" % (CFG["ip"],CFG["port"])
        self.log(message)
        # Pico.set_debug(True)
        pico.DEBUG[0] = CFG["debug"]
        self.log("start() - Debug=" + str(pico.DEBUG))
        web = Webserver(CFG["ip"],CFG["port"])
        web.run(self.handler)

    def init_route(self):
        """
        init_route() - Initializes the routes for PATH request.
        """
        self.route = {
            "/"               : self.webpage,
            "/web"            : self.webpage,

            # Send file
            "/pico.css"       : ["css","html/pico.css"],
            "/favicon.svg"    : ["svg","html/favicon.svg"],
            "/favicon.ico"    : ["svg","html/favicon.svg"],
            "/favicon.png"    : ["png","html/favicon.png"],
            "/kamP.svg"       : ["svg","html/kamP.svg"],

            # Output of FHEM String:
            "/pico/fhem/temp" : Temp.fhem_string,
            "/pico/fhem/volt" : Power.fhem_string,
            "/pico/fhem/flash": Flash.fhem_string,
            "/pico/fhem/name" : Name.fhem_string,
            "/pico/fhem/mem"  : Mem.fhem_string,
            "/pico/fhem/reed" : [Reed.fhem_string,CFG["reed"]],

            # Execute command:
            "/pico/led/on"    : self.led.on,
            "/pico/led/off"   : self.led.off,
            "/pico/led/toggle": self.led.toggle,

            # Execute command originated from  Website:
            "/web/led/on"     : ["html", self.led.on, self.webpage],
            "/web/led/off"    : ["html", self.led.off, self.webpage],
            "/web/led/toggle" : ["html", self.led.toggle, self.webpage],

            # Execute a system command:
            "/web/shutdown"   : System.cmd_exit,
            "/pico/reset"     : System.cmd_reset,
            "/pico/soft_reset": System.cmd_soft_reset,
            "/pico/gc"        : ["html", Mem.cmd_gc, self.webpage],
        }

# What are the possibilities:
# - Function: Function must return array [type, string],
#   i.e. ["txt", <fhem_string>]
#   i.e. ["html", <web_string>]
# - Array 2 [type,text]: Direct to Webserver
# - Array 2 [type,func]: Function must return array [type, string],
# - Array 3 [type,func1,func2]: Function2 must return array [type,string]

# -------------------------------------------------------
