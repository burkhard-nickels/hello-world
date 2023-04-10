
Files for Pico Project
------------------------
Pico/boot.py    - Loaded from Pico after Boot (Set sys.path for modules).
Pico/main.py    - Startet from Pico after Boot (Start main application).
Pico/pico.cfg   - Config file for Application

Pico/scripts/color.sh - Create colored Sourcecode file for Webpage.
Pico/scripts/env.sh   - Set Python Library Path.
Pico/scripts/test.sh  - Start all tests locally on your debian linux.
Pico/scripts/minicom.sh - Serial connection to Pico.
Pico/scripts/rshell.sh  - Rshell connection to Pico.
Pico/scripts/rshell-copy-all.sh - Copy all files to Pico via rshell.

Pico/html/            - Folder for Web files.
Pico/html/favicon.svg - Favicon file.
Pico/html/pico.css    - CSS file.
Pico/html/kamP.svg    - Image for Webpage.

Pico/doc/             - Folder for documentation, examples or additional files.
Pico/doc/README.txt   - Some information.

Pico/test/            - Folder for test files.
Pico/test/test.cfg    - For testing module lib/base/config.py

Pico/lib/             - Folder for Python Modules.
Pico/lib/httpd.py     - Main Application.
Pico/lib/app.py       - Choosing applicaton to test or start.

Pico/lib/base/             - Folder for basic classes.
Pico/lib/base/__init__.py  - Needed for Python Package.
Pico/lib/base/config.py    - Read config file.
Pico/lib/base/device.py    - Base class for Devices.
Pico/lib/base/pico.py      - Base class for Pico

Pico/lib/device/             - Folder for device classes (external hardware).
Pico/lib/device/__init__.py  - Needed for Python Package.
Pico/lib/device/led.py       - External or Internal LED.
Pico/lib/device/power.py     - External battery or internal Power.
Pico/lib/device/reed.py      - External Reed Contact.

Pico/lib/dummy/              - Folder for Pico dummy classes for local test.
Pico/lib/dummy/gc.py         - Dummy for Pico gc module.
Pico/lib/dummy/machine.py    - Dummy for Pico machine module.
Pico/lib/dummy/network.py    - Dummy for Pico network module.

Pico/lib/net/                - Folder for network classes.
Pico/lib/net/__init__.py     - Needed for Python Package.
Pico/lib/net/client.py       - Client for testing.
Pico/lib/net/server.py       - Network Server.
Pico/lib/net/wlan.py         - Creates Wlan Connection on Pico.

Pico/lib/system/             - Folder for Pico system classes.
Pico/lib/system/__init__.py  - Needed for Python Package.
Pico/lib/system/flash.py     - Internal Flash Memory.
Pico/lib/system/system.py    - Internal Systemname, Memory.
Pico/lib/system/temp.py      - Internel Temperature Sensor.

Pico/lib/web/                - Folder for Web classes.
Pico/lib/web/__init__.py     - Needed for Python Package.
Pico/lib/web/html.py         - Class Html (i.e. main html)
Pico/lib/web/http.py         - Class Http
Pico/lib/web/webserver.py    - Class Webserver <- Server <- Pico

