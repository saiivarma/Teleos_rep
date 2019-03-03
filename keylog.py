from pynput.keyboard import Key,Listener
from pynput.mouse import Listener as lis
from win32gui import GetWindowText,GetForegroundWindow
import time
from datetime import datetime
import pandas as pd
import sys
import db_keylog as db 
import clean
import file_type
arg=0
for cmd in sys.argv:
    arg=cmd

log=[]
listen = []
int_time= 10
terminate_time=20 #change to 10 mins i.e.600

prev_time =time.time()
total_time= prev_time

app_time = prev_time

prev_window = ''

def cleaned_data_to_database(log):
    global prev_time
    global arg
    
    if time.time()-prev_time>= int_time:
        prev_time=time.time()
        
        data = clean.clean(log)
        log = []

        data = file_type.get_file_type(data)

        #print(data)
        
        oplist=[]
        for i in range(0,len(data)):

            oplist.append([502,data['time'][i],data['clicks'][i],data['file cat'][i], data['file name'][i]])
        db.update(db.get_overall("502"), oplist, datetime.now().date())
        
        ## sedn data to databas
        
        print('------')
        print(pd.DataFrame(oplist))
       # print(data['file name'][0])
        print('------')

        '''if time.time() - total_time >= terminate_time:
            key_Listener.stop()##
            listener.stop()##'''
    return log  
    

def focus_win():
    file_name = GetWindowText(GetForegroundWindow())
    file_name = file_name.lower()
    return file_name

def window_changed():
    global app_time
    present = focus_win()
    time_spent = time.time() - app_time
    app_time = time.time()
    log.append([present,1, time_spent])

def on_press(key):
    global log
    listen.append(key)
    
    #print(key)
    window_changed()
    #print(log)
    log = cleaned_data_to_database(log)
               
def on_click(x, y, button, pressed):
    global log
    if pressed:
        #print(button,' Pressed at' ,(x,y))
        time.sleep(0.5)
        listen.append(str(button)) ##not used
       
        window_changed()
        #print(log)
        log = cleaned_data_to_database(log)         
                
key_Listener = Listener(on_press=on_press)
key_Listener.start()

# Collect events until released
with lis(on_click=on_click) as listener:
    listener.join()


      

