import subprocess
#cmd = r"scp -i ~/.ssh/id_rsa /home/pi/Desktop/data/kuroda_data.csv pi@35.189.138.28:/home/pi/data"
cmd = r"scp -i ~/.ssh/id_rsa /home/pi/Desktop/data/My_data.csv pi@35.189.138.28:/home/pi/data"
subprocess.call(cmd.split())

import os
os.system("python run_python_on_gcp.py")
os.system("python3 popup.py")