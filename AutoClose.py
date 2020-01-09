import ctypes 
import threading 
import time 
#ctypes.windll.user32.MessageBoxA(0, 'test', "Reminding", 0) 

def worker(title,close_until_seconds): 
    time.sleep(close_until_seconds) 
    wd=ctypes.windll.user32.FindWindowA(0,title) 
    ctypes.windll.user32.SendMessageA(wd,0x0010,0,0) 
    return 

def AutoCloseMessageBoxW(text, title, close_until_seconds): 
    print(text)
    t = threading.Thread(target=worker,args=(title,close_until_seconds)) 
    t.start() 
    ctypes.windll.user32.MessageBoxA(0, text, title, 0) 


AutoCloseMessageBoxW('inprogress','TEST_CLOSE',3)