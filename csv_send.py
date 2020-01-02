import subprocess
cmd = r"scp -i ~/.ssh/id_rsa /home/pi/Desktop/data/XXXXXX_data.csv pi@XX.XXX.XXX.XX:/home/pi/data"
subprocess.call(cmd.split())

import os
os.system("python3 popup.py")