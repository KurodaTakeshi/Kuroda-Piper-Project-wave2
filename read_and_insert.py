import csv
import datetime
import psycopg2

conn = psycopg2.connect(host='IP Adress', dbname='XXXXX', user='XXXXX', password='XXXXX', port=XXXXX)
cursor = conn.cursor()
cursor.execute("DELETE FROM XXXX_table;")

import glob

for file in glob.glob("/home/pi/data/*.csv"):
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            tstr1 = row[3]
            tstr2 = row[4]
            tdatetime1 = datetime.datetime.strptime(tstr1, '%Y/%m/%d %H:%M:%S')
            tdatetime2 = datetime.datetime.strptime(tstr2, '%Y/%m/%d %H:%M:%S')
            second = tdatetime2 - tdatetime1
            second = second.total_seconds()
            second = int(second)
            row.append(second)
            temp1 = row[0]
            temp2 = row[1]
            temp3 = row[2]
            temp4 = row[3]
            temp5 = row[4]
            temp6 = row[5]
            cursor.execute("INSERT INTO XXXX_table (date,name,task,start_at,finish_at,second) VALUES (%s,%s,%s,%s,%s,%s)",(temp1,temp2,temp3,temp4,temp5,temp6))

conn.commit()
cursor.close()
conn.close()
