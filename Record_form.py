import datetime
import time
import csv
import sys
import tkinter
import tkinter.ttk as ttk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

flg = 0

dt_now1 = datetime.datetime.now()

def foo():
    task = t.get()
    flg = 1
    if flg == 1:
        dt_now2 = datetime.datetime.now()
        logDate = dt_now1.strftime("%Y/%m/%d")
        myname = 'My_Name'
        list =[logDate,myname,task,dt_now1.strftime('%Y/%m/%d %H:%M:%S'),dt_now2.strftime('%Y/%m/%d %H:%M:%S')]
        
        try:
            with open(r"/home/pi/Desktop/data/My_data.csv",'a', newline="") as f:
                writer = csv.writer(f)
                writer.writerow(list)
        except FileNotFoundError:
            messagebox.showinfo('Not Found', 'CSV file not found' + '\n' + 'Start_at: ' + str(dt_now1))
        except PermissionError:
            messagebox.showinfo('Permission Error', 'CSV file is not closed' + '\n' + 'Start_at: ' + str(dt_now1))
        root.quit()

root = Tk()
root.title('Record form')
frame1 = ttk.Frame(root)
label1 = ttk.Label(frame1, text='Measuring time...')
label2 = ttk.Label(frame1, text='Please enter the task before finishing.\nAfter entering the task, click the OK button to finish')

t = StringVar()
 
entry1 = ttk.Entry(frame1, textvariable=t, justify="left", width=70)
button1 = ttk.Button(frame1, text='OK', command=foo)
frame1.grid(row=0,column=0,sticky=(N,E,S,W))
label1.grid(row=1,column=1,sticky=W)
label2.grid(row=2,column=1,sticky=W)
entry1.grid(row=3,column=1,sticky=W)
button1.grid(row=4,column=1,sticky=W)

pngfile=PhotoImage(file=r"/home/pi/Desktop/image/image.png")
cv=Canvas(bg="white",width=200-1,height=200-1)
cv.create_image(1,1,image=pngfile,anchor=NW)
cv.grid(row=0, column=1)


for child in frame1.winfo_children():
    child.grid_configure(padx=50, pady=10)

root.mainloop()
