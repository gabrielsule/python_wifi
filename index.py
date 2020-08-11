import subprocess

def getWifi():
    res = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    res = res.decode('utf-8').split('\n')

    for i in res:
        if 'Perfil de todos los usuarios' in i:
            wifi = i.split(':')[1]
            print(wifi)
            wifi = wifi.replace('\r', '').strip()
           
            getPwd(wifi)
            

def getPwd(_wifi):
    res = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', _wifi, 'key=clear'])
    res = res.decode('utf-8', errors="backslashreplace").split('\n')

    for i in res:
        if 'Contenido de la clave' in i:
            pwd = i.split(':')[1]
            print(pwd)


getWifi()
