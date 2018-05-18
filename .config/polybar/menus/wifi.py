#!/usr/bin/env python3

from subprocess import Popen, PIPE

def getPopenObject(commands,arguments=[]):
    commands.extend(arguments)
    obj = Popen(
        commands,
        stdin=PIPE,
        stdout=PIPE
    )
    return obj

def listWifis():
    available = ['nmcli','device','wifi']
    listAvailable = getPopenObject(available)
    stdout = listAvailable.communicate()[0].decode("utf-8").rstrip()

    if listAvailable.returncode == 1:
        return None
    else:
        return stdout[stdout.index('\n')+1:]

def status():
    wifiStatus = ['nmcli','radio','wifi']
    status = getPopenObject(wifiStatus)
    stdout = status.communicate()[0].decode("utf-8").rstrip()

    if status.returncode == 1:
        return None
    else:
        return stdout == 'enabled'

def toggleWifi():
    wifi = ['nmcli','radio','wifi']
    if status():
        toggle = getPopenObject(wifi,['off'])
    else:
        toggle = getPopenObject(wifi,['on'])
    toggle.communicate()
    
def rescan():
    refresh = ['nmcli','device','wifi','rescan']
    ref = getPopenObject(refresh)
    ref.communicate()

def connect(SSID,PASS=''):
    connect = ['nmcli','device','wifi','connect',SSID,'password',PASS]
    if not PASS:
        con = getPopenObject(connect)
    else:
        con = getPopenObject(connect)
    stdout = con.communicate()[0].decode("utf-8").rstrip()
    
    return "Error:" in stdout

""" 
available = ['nmcli','device','wifi','list']
wifiStatus = ['nmcli','radio','wifi']
wifiOn = ['nmcli','radio','wifi','on']
wifiOff = ['nmcli','radio','wifi','off']
refresh = ['nmcli','device','wifi','rescan']
connect = ['nmcli','device','wifi','connect',SSID]
connectPass = ['nmcli','device','wifi','connect',SSID,PASS] """

print(connect("Helm's Deep2","naovaiterlol"))