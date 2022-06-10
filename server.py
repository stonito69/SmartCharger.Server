#!/usr/bin/env python

import socketserver, subprocess, sys
from threading import Thread
from pprint import pprint
import json
from datetime import datetime
import time
from enum import Enum
import urllib.request as urllib2
from rpi_rf import RFDevice


class State(Enum):
    Unknown = 1
    Charging = 2
    Discharging = 3
    Full = 4
    NotCharging = 5
    NotPresent = 6

with open('/home/pi/server.config','r') as f:
    config = json.load(f)
HOST = config["Host"]
PORT = config["Port"]


last_log=""

def write_log(message):
    global last_log
    print (time.strftime('%H:%M:%S ')+" : "+message)
    if last_log!=message:
        filename = time.strftime("%Y-%m-%d")+'.txt';
        timestr = time.strftime('%H:%M:%S ')
        file_object = open('/home/pi/log/'+filename, 'a')
        file_object.write(timestr+message+"\r\n")
        file_object.close()
        last_log=message

class SingleTCPHandler(socketserver.BaseRequestHandler):
    "One instance per connection.  Override handle(self) to customize action."
    def handle(self):
        data = self.request.recv(1024)  # clip input at 1Kb
        text = data.decode('utf-8')
        msg=json.loads(text)
        if 'cmd' in msg.keys():
            if (msg['cmd']=='onoff'):
                if (msg['on']==True): 
                    write_log('MAN ON')
                    smartcharger.on()
                    self.request.send(bytes("OK/r/n", 'UTF-8'))
                else: 
                    write_log('MAN OFF')
                    smartcharger.off()
                    self.request.send(bytes("OK/r/n", 'UTF-8'))
            elif (msg['cmd']=='status'):
                write_log('BAT {0} {1}'.format(State(msg['state']),msg['level']))
                smartcharger.batteryUpdate(msg['level'],msg['state'])
                self.request.send(bytes("OK/r/n", 'UTF-8'))
            elif (msg['cmd']=='get_config'):
                self.request.send(bytes(json.dumps(config),'UTF-8'))
            elif (msg['cmd']=='set_config'):
                config["BatteryMax"]=msg['max']
                config["BatteryMin"]=msg['min']
                config["PingMinutes"]=msg['ping']
                self.request.send(bytes("OK/r/n", 'UTF-8'))
                with open('/home/pi/server.config','w') as f:
                    json.dump(config,f)
                
        self.request.close()

class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

class SmartCharger:
    def __init__(self):
        self.ping=datetime.now()
        self.isOn=True
        self.rfdevice = RFDevice(15)
        self.rfdevice.enable_tx()
        self.rfdevice.tx_repeat = 10

    def batteryUpdate(self,level,state):
        self.level=level
        self.state=state
        self.isOn = (state == 2) or (state == 4)
        self.ping=datetime.now()
        if self.isOn:
            if level>=config['BatteryMax'] or level==1: 
                write_log('AUT OFF')
                self.off()
        else:
            if level<=config['BatteryMin']: 
                write_log('AUT ON')
                self.on()
    def seconds_to_last_ping(self):
        return (datetime.now()-self.ping).total_seconds()
    def on(self):
        if not self.isOn:
            self.rfdevice.tx_code(3671900, 4)
            #os.system('rpi-rf_send -g 15 -t 4 ')
            self.isOn=True
    def off(self):
        if self.isOn:
            self.rfdevice.tx_code(3985788, 4)
            #os.system('rpi-rf_send -g 15 -t 4 3985788')
            self.isOn=False


def timer(n=5):
    while True:
        if smartcharger.seconds_to_last_ping() > (config["PingMinutes"]*60*2.5):
            write_log('PING ON '+str(smartcharger.seconds_to_last_ping()))
            smartcharger.on()
        time.sleep(n)

smartcharger=SmartCharger()

thread = Thread(target=timer, daemon=True)
thread.start()

def wait_for_internet_connection():
    while True:
        try:
            response = urllib2.urlopen('http://192.168.0.1',timeout=1)
            return
        except urllib2.URLError:
            pass


if __name__ == "__main__":
    write_log("server starting")
    wait_for_internet_connection()
    write_log("network working")
    time.sleep(5)
    server = SimpleServer((HOST, PORT), SingleTCPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        write_log("server closing")
    



