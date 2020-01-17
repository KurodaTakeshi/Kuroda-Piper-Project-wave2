import os

os.system("ssh pi@35.189.138.28 -i ~/.ssh/id_rsa python read_and_insert.py")
os.system("python notification_webhook.py")