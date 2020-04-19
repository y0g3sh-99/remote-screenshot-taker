#Author: Yogesh Ingale

import time
import socket
import os
import glob
import pyautogui

def send_screenshot(conn):
    filename = time.ctime() + ".jpeg"
    filename = filename.replace(':', '.')
    sc=pyautogui.screenshot(filename)
    conn.sendall(filename)
    f=open(filename,"rb")
    data=f.read()
    conn.sendall(data)
    f.close()
    os.remove(filename)
    print ("Sent screenshot %s")%filename

try:
    s=socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0",54321))
    s.listen(5)
    print ("Server listening...")
    while True:
        conn, addr = s.accept()
        print ("Client connected: %s") % addr[0]
        choice = conn.recv(10)
        if int(choice) == 1:
            try:
                send_screenshot(conn)
            except:
                break
        elif int(choice) == 2:
            interval = int(conn.recv(10))
            while True:
                try:
                    send_screenshot(conn)
                    time.sleep(interval)
                    temp=conn.recv(3)
                except:
                    break
        print ("%s got disconnected")%addr[0]
        for i in glob.glob("*.jpeg"):
            os.remove(i)
            
except:
    s.close()
            
        
