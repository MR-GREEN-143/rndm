import os, platform

os.system('xdg-open https://www.facebook.com/profile.php?id=100084131360050')

try:

        import requests

except:

        os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from rndm  import main

        main()
#32
elif bit == "32bit":

        from rndm32 import main

        main()
