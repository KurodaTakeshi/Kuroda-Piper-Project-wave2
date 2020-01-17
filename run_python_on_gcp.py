import os

os.system("ssh hoge@IP Adress -i ~/.ssh/id_rsa python read_and_insert.py")
os.system("python notification_webhook.py")
