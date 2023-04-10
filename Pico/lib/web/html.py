"""
Module html - HTML Code
"""

class Html():
    """
    Class Html - Generic HTML
    """
    def __init__(self, host, port):
        """
        Html() - Constructor
        """
        super().__init__()
        self.host = host
        self.port = port

    # ------------- Table -------------------
    @staticmethod
    def table(clazz,cont):
        """
        table(content) - Creates a HTML table element.
        """
        html = "<table class=\"" + clazz + "\">" + cont + "</table>\n"
        return html

    @staticmethod
    def tr(clazz,cont):
        """
        tr(content) - Creates a HTML tr (table row) element.
        """
        html = "<tr class=\"" + clazz + "\">" + cont + "</tr>\n"
        return html

    @staticmethod
    def td(clazz,cont):
        """
        td(content) - Creates a HTML td (table cell) element.
        """
        html = "<td class=\"" + clazz + "\">" + cont + "</td>\n"
        return html

    # --------------- Main ------------------
    def main(self,title,text):
        """
        main(title,text) - Creates a Main HTML document.
        """
        html = self.main_base(title,text,1)
        return html

    def main_error(self):
        """
        main_error(title,text,refresh) - Creates a HTML document with Error message "Not Found".
        """
        html = self.main_base("ERROR", "<div class=error>Error: URL Not Found!</div>",0)
        return html

    def main_base(self,title,text,refresh):
        """
        main_base(title,text,refresh) - Creates a HTML document.
        """
        html = "<!DOCTYPE html>\r\n"
        html += "<html>\n"
        html += "  <head><title>Pico W (" + self.host + ")</title>\n"
        if refresh:
            html += "  <meta http-equiv=\"refresh\" content=\"30\">\n"
        html += "  <link rel=\"stylesheet\" href=\"/pico.css\">\n"
        html += "  <link rel=\"shortcut icon\" type=\"image/svg+xml\" "
        html += "href=\"http://" + self.host + ":" + str(self.port) + "/favicon.svg\">\n"
        html += "  <link rel=\"shortcut icon\" type=\"image/png\" "
        html += "href=\"http://" + self.host + ":" + str(self.port) + "/favicon.png\">\n"
        html += "</head>\n"
        html += "<body><center>\n"
        html += "  <table class=\"title\"><tr><td width=\"10%\">\n"
        html += "    <img class=\"title_image\" width=\"100px\" src=\"/favicon.svg\">\n"
        html += "  </td><td width=\"90%\">\n"
        html += "  <h1>\n"
        html += "    <span class=\"hsmall\"> Pico W </span>\n"
        html += "    <span class=\"hlarge\"> " + title + " </span>\n"
        html += "  </h1>\n"
        html += "  </td></tr></table>\n"
        html += text + "\n"
        html += "</body></html>\r\n\r\n"
        return html

# -----------------------------------------------------------------------------------
