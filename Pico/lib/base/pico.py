"""
Module pico - Contains base class for all Classes.
"""
from time import localtime

DEBUG = [None]

class Pico():
    """
    Class Pico - Base Class for all Classes on Pico.
    """

    Debug_func = print

    def __init__(self):
        """
        Pico() - Constructor
        """
        self.log("Pico() Start debug=" + str(DEBUG))

    @staticmethod
    def timestamp():
        """
        timestamp() - Get a Timestamp for loggin.
        """
        # MicroPython and Python have differnt number (8 -> 9)
        # (year,month,mond,hour,minute,sec,_,_) = localtime()
        # (year,month,mond,hour,minute,sec,weekd,yeard) = localtime()
        # (year,month,mond,hour,minute,sec,weekd,yeard,dst) = localtime()
        # timestamp = "%4d.%02d.%02d-%02d:%02d:%02d" % (year,month,mond,hour,minute,sec)

        time = list(localtime())
        timestamp = "%4d.%02d.%02d-%02d:%02d:%02d" % (time[0],time[1],time[2],
            time[3],time[4],time[5])
        return timestamp

    def debug_no_endl(self,txt):
        """
        debug_no_endl() - Debug without Newline.
        """
        self.debug(txt,endl='')

    def log(self,txt):
        """
        log() - Log.
        """
        timestamp = Pico.timestamp()
        clazz = self.__class__.__name__
        Pico.Debug_func(timestamp + " LOG " + clazz + ":: " + txt)

    def error(self,txt):
        """
        error() - Error.
        """
        timestamp = Pico.timestamp()
        clazz = self.__class__.__name__
        Pico.Debug_func(timestamp + " ERROR " + clazz + ":: " + txt)

    def debug(self,txt, endl='\n'):
        """
        debug() - Debug.
        """
        timestamp = Pico.timestamp()
        clazz = self.__class__.__name__
        if DEBUG:
            Pico.Debug_func(timestamp + " DEBUG " + clazz + ":: " + txt, end=endl)

# --------------------- Test purposes -----------------------
    @staticmethod
    def test():
        """
        test() - Test of debug() Methods
        """
        obj = Pico()
        obj.debug("Debug: DEBUG=False")
        obj.error("Error: DEBUG=False")
        obj.log("Log: DEBUG=False")
        global DEBUG
        DEBUG = True
        print(__class__.__name__)
        print(__class__)
        print(__name__)
        obj.debug("Debug: DEBUG=True")
        obj.error("Error: DEBUG=True")
        obj.log("Log: DEBUG=True")
        Pico.Debug_func = Pico.print_function
        obj.debug("Debug: External Func")
        obj.error("Error: External Func")
        obj.log("Log: External Func")

    @staticmethod
    def print_function(txt,end='\n'):
        """
        print_function() - Reference for differnet printing.
        """
        print("EXTERN: " + txt,end=end)

# ----------------------------------------------------------
