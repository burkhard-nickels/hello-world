
awd=`pwd`

rshell mkdir /pyboard/lib/base /pyboard/lib/device /pyboard/lib/net /pyboard/lib/system /pyboard/lib/web /pyboard/html

rshell cp lib/base/*.py /pyboard/lib/base
rshell cp lib/device/*.py /pyboard/lib/device
rshell cp lib/net/*.py /pyboard/lib/net
rshell cp lib/system/*.py /pyboard/lib/system
rshell cp lib/web/*.py /pyboard/lib/web

rshell cp boot.py /pyboard/
rshell cp lib/httpd.py /pyboard/lib
rshell cp local/pico.cfg /pyboard/

rshell cp html/pico.css /pyboard/html
rshell cp html/kamP.svg /pyboard/html
rshell cp html/favicon.svg /pyboard/html

