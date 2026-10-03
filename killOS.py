from binascii import a2b_qp
from logging import root
from math import e
import platform
import shutil
import subprocess
import time
import locale
import psutil
import sys
import os
import requests
import webbrowser
import pyautogui
import random
from colorama import *
import winsound
from pathlib import Path
import winreg as reg
import sys

class usercreate:
    def __init__(self, username, usermode, password):
        self.username = username
        self.usermode = usermode
        self.password = password

class userfilesystemPermission:
    def __init__(self, userType, PermissionUser):
        self.userType = userType
        self.PermissionUser = PermissionUser

class system_permisson:
    def __init__(self, permission, object, nova_rate):
        self.permission = permission
        self.object = object
        self.nova_rate = nova_rate

#data
cpu = platform.processor()
ram = round(psutil.virtual_memory().total / (1024 ** 3), 1)
gpu = subprocess.getoutput('powershell "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"').strip()
loc = locale.getdefaultlocale()[0]
us = os.getlogin()
user = "root"
usermodee = [0, 1, 2, 3, 4]
if user == "root":
    usermode = 1
else:
    usermode = 0
User = usercreate("root", usermode, 123321)
User.username = user
usercustom = User
textcreate = ""
sysinfo = {
    "CPU": f"{cpu}",
    "RAM": f"{ram}",
    "GPU": f"{gpu}",
    "OS": "KILL OS (linux)"
}
novacontactmail = "nova@killos.org"
rootdir = Path("C:/killOS")
filesystem = [
    rootdir / "releases",
    rootdir / "boot" / "killos",
    rootdir / "boot" / "mnt",
    rootdir / "mnt",
    rootdir / "setup",
    rootdir / "root",
    rootdir / "etc",
    rootdir / "killos" / "mnt",
    rootdir / "lib",
    rootdir / "pacman"]
for folder in filesystem:
    folder.mkdir(parents=True, exist_ok=True)
forboot = Path(sys.argv[0]).resolve()
forbootdir = rootdir / "boot" / "killos"
sett = forbootdir / forboot.name
if not sett.exists():
    shutil.copy2(forboot, sett)
session_time = time.time()
error = "KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e"
DNS = 1111, 8080
yayactive = False
googleinstall = False
directory = ""
cd_list = ["boot", "user", "setup", "root", "etc",  "lib", "killos", "pacman"]
boot_list = ["killos", "mnt", "bootloader.sh", "NOVA_permission.daemon"]
lib_list = [f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin", f"{random.randint(1, 99999)}.bin"]
systemversion = "KILL OS 3.1 Arch Linux 7.2.3.arch1-3"
googleflag = False
coreflag = False
killos32flag = False
filesystemkillos = "packets", "pacman", "mnt", "core.conf", "killos.sh", "Not for read", "req.txt"
PermissionE = "Permission denied."
id = "1root"
killosfilesystem = userdefaultPermission = userfilesystemPermission("1root", 1)
statusconf = False
usercustom = usercreate("root", 1, 123321)
permissionnovafileactions = False
cdboot = False
ss = '''
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
'''
bootflag = False
key = "NOVA-543-NOVA"



symbols = ['ø', 'Ø', 'ɸ', 'Œ', 'ɶ']
for i in range(30):
    print(f"\rLOADING...{symbols[i % len(symbols)]}", end="")
    time.sleep(0.1)
print("\nLOADED")
pyautogui.hotkey('f11')
print("\nRunning...")
time.sleep(1)
print("password?")
password = input()
if password == "123321":
    print("\rAccess granted")
else:
    print("\rAccess denied")
    print(f"\runmount... {symbols[i % len(symbols)]}", end=" ")
    time.sleep(4)
    exit()
for i in range(30):
    print(f"\rLOADING...{symbols[i % len(symbols)]}", end="")
    time.sleep(0.1)
print(f"\rLOADING SYSTEM...{symbols[i % len(symbols)]}", end="")
time.sleep(0.1)
print("\nSYSTEM LOADED")
print("\nNOVA key? 'pass' to enter the free edition")
key2 = input()
if key2 == key:
    print("\rgranted")
elif key2 == "pass":
    print("\rgranted")
else:
    print("\rdenied")
    exit()
print("\nRunning system...")
time.sleep(1)
print("System run.")
print(f"{Fore.RED} $$\   $$\ $$$$$$\ $$\       $$\              $$$$$$\   $$$$$$\  ")
print(f"{Fore.RED} $$ | $$  |\_$$  _|$$ |      $$ |            $$  __$$\ $$  __$$\ ")
print(f"{Fore.RED} $$ |$$  /   $$ |  $$ |      $$ |            $$ /  $$ |$$ /  \__|")
print(f"{Fore.RED} $$$$$  /    $$ |  $$ |      $$ |  --------  $$ |  $$ |\$$$$$$\  ")
print(f"{Fore.RED} $$  $$<     $$ |  $$ |      $$ |            $$ |  $$ | \____$$\ ")
print(f"{Fore.RED} $$ |\$$\    $$ |  $$ |      $$ |            $$ |  $$ |$$\   $$ |")
print(f"{Fore.RED} $$ | \$$\ $$$$$$\ $$$$$$$$\ $$$$$$$$\        $$$$$$  |\$$$$$$  |")
print(f"{Fore.RED} \__|  \__|\______|\________|\________|       \______/  \______/ ")
print(f"{Fore.WHITE}")
print(" KILL OS linux menu. os based linux")

print("\r sectors: boot, home")
print("\r 1: boot 2: home")
choice = int(input("\rsector?/: "))
if choice == 1:
    print("\rBooting...")
    time.sleep(3)
    print(f"{Fore.GREEN}[ ✓ ] found sector in disk")
    print(f"{Fore.GREEN}[ ✓ ] found boot sectors 1/3")
    time.sleep(1)
    print(f"{Fore.GREEN}[ ✓ ] found boot sectors 2/3")
    time.sleep(3)
    print(f"{Fore.GREEN}[ ✓ ] found boot sectors 3/3")
    print(f"{Fore.GREEN}[ ✓ ] boot sectors found")
    print(f"{Fore.WHITE}")
    print(f"{Fore.RED}[ x ] load in RAM")
    print(f"{Fore.RED}[ x ] try to loading in RAM")
    print(f"{Fore.WHITE}")
    print(f"{Fore.GREEN}[ ✓ ] file bootloader /boot")
    print(f"{Fore.WHITE}")
    time.sleep(3)
    print("\r                        $$\                                                               ")
    print("\r                        $$ |                                                               ")
    print("\r$$\  $$\  $$\  $$$$$$\  $$ | $$$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\                    ")
    print("\r$$ | $$ | $$ |$$  __$$\ $$ |$$  _____|$$  __$$\ $$  _$$  _$$\ $$  __$$\                   ")
    print("\r$$ | $$ | $$ |$$$$$$$$ |$$ |$$ /      $$ /  $$ |$$ / $$ / $$ |$$$$$$$$ |                  ")
    print("\r$$ | $$ | $$ |$$   ____|$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$   ____|                  ")
    print("\r\$$$$$\$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$  |$$ | $$ | $$ |\$$$$$$$\                    ")
    print("\r\_____\____/  \_______|\__| \_______| \______/ \__| \__| \__| \_______|                   ")
    print("\r                                                                                          ")
    print("\r                                                                                          ")
    print("\r                                                                                          ")
    print("\r                                                                                          ")
    print("\r                                                                                           ")
    print("\r$$$$$$\ $$$$$$\ $$$$$$\ $$$$$$\ $$$$$$\ $$$$$$\ $$$$$$\ $$$$$$\                           ")
    print("\r\______|\______|\______|\______|\______|\______|\______|\______|                          ")
    print("\r                                                                                          ")
    print("\r                                                                                          ")
    print("\r                                                                                          ")
    print("\r                                                                                          ")
    print("\r                                                                                          ")
    print("\r                                                                                          ")
    print("\r  $$\                    $$\   $$\ $$$$$$\ $$\       $$\              $$$$$$\   $$$$$$\  ")
    print("\r  $$ |                   $$ | $$  |\_$$  _|$$ |      $$ |            $$  __$$\ $$  __$$\ ")
    print("\r$$$$$$\    $$$$$$\       $$ |$$  /   $$ |  $$ |      $$ |            $$ /  $$ |$$ /  \__|")
    print("\r\_$$  _|  $$  __$$\      $$$$$  /    $$ |  $$ |      $$ |            $$ |  $$ |\$$$$$$\  ")
    print("\r $$ |    $$ /  $$ |      $$  $$<     $$ |  $$ |      $$ |            $$ |  $$ | \____$$\ ")
    print("\r $$ |$$\ $$ |  $$ |      $$ |\$$\    $$ |  $$ |      $$ |            $$ |  $$ |$$\   $$ | ")
    print("\r \$$$$  |\$$$$$$  |      $$ | \$$\ $$$$$$\ $$$$$$$$\ $$$$$$$$\        $$$$$$  |\$$$$$$  |")
    print("\r  \____/  \______/       \__|  \__|\______|\________|\________|       \______/  \______/ ")
    print("\r                                                                                          ")
    print("\r                                                                                          ")
    print("\rBooted/mount")
    time.sleep(1)
    while True:
        print("\r'help' to commands")
        command = input(f"/{directory}/{user}@ ")
        if command == "help":
            print("\r 1 lsblk")
            print("\r 2 exit")
            print("\r 3 unmount")
            print("\r 4 cd <directory>")
            print("\r 5 kill os")
            print("\r 6 pacman -S google-chrome")
            print("\r 7 sudo pacman -Syu")
            print("\r 8 shutdown")
            print("\r 14 boot={directory}")
            print("\r 9 reboot")
            print("\r 10 help")
            print("\r ⟬nova conf edit⟭")
            print("\r 11 sudo useradd")
            print("\r 12 dolphin")
            print("\r 13 sudo userdel")
            print("\r 14 sudo usermod")
            print("\r 15 sudo userpassw")
            print("\r 16 mkdir -s text | or 'cat'")
            print("\r 17 mkdir -r text")
            print("\r 63 ls -l /killos/killos.sh")
            print("\r 64 cat /killos/mnt/nova.conf")
            print("\r 18 display")
            print("\r 19 ls")
            print("\r 20 cmatrix")
            print("\r 35 cat /killos/core.conf")
            print("\r 20 bash")
            print("\r 21 ffmpeg")
            print("\r 22 server")
            print("\r 23 ping")
            print("\r 45 boot from another directory")
            print("\r 24 status")
            print("")
            print("      connect")
            print("")
            print("\r 42 status killos.sh")
            print("\r 25 config")
            print("\r 26 sudo pacman -S yay")
            print("\r 27 uninstall yay")
            print("\r 28 cd")
            print("\r 38 cat /killos/killos.sh")
            print("\r 29 whoami")
            print("\r NOVAmenu")
            print("\r 38 cat /killos/req.txt")
            print("\r 30 id")
            print("\r 31 pwd")
            print("\r 32 uname -a")
            print("\r 33 pacman -Q")
            print("\r 34 google-chrome")
            print("\r 35 free -h")
            print("\r 36 ls -la /killos")
            print("\r 39 ls -ld /killos")
            print("\r 40 file /killos/killos.sh")
            print("\r 43 ls <direcroty>")
            print("\r 44 cat /etc/os-release")
            print("\r 46 mnt /boot")
            print("\r 47 bootloader mode")
            print("\r 49 minigame")
            print("\r 50 releases")
            print("\r 51 bootloader mode --dis")
            print("\r 52 bootloader mode --en")
            
            

        elif command == "lsblk":
            print("\r | partition |")
            print("\r | /boot  512MB  mount |")
            print("\r | /nvme0n1p1  65G   mount |")
        elif command == "exit":
                    print("\r[  ] unmounting")
                    print("\r[  ] unmounting /boot")
                    time.sleep(4)
                    print(f"{Fore.GREEN}[ ✓ ] unmounting")
                    print(f"{Fore.GREEN}[ ✓ ] unmounting /boot")
                    print(f"{Fore.GREEN}[ ✓ ] unmounting /boot/killos")
                    print(f"{Fore.GREEN}[ ✓ ] unmounting /nvme0n1p1")
                    print(f"{Fore.WHITE}")
                    time.sleep(3)
                    exit()
        elif command == "unmount":
            print("\r[  ] unmounting")
            print("\r[  ] unmounting /boot")
            time.sleep(4)
            print(f"{Fore.GREEN}[ ✓ ] unmounting")
            print(f"{Fore.GREEN}[ ✓ ] unmounting /boot")
            print(f"{Fore.GREEN}[ ✓ ] unmounting /boot/killos")
            print(f"{Fore.GREEN}[ ✓ ] unmounting /nvme0n1p1")
            print(f"{Fore.WHITE}")
            time.sleep(3)
            exit()
        elif command == "python":
            print("\r[  ] starting python")
            time.sleep(3)
            print("\r[ ✓ ] started python")
            time.sleep(1)
            subprocess.run(["python3"])
        elif command == "kill os":
            print("\r                linux: killOS")
            print(f"\r $$\   $$\               CPU: {cpu}")
            print(f"\r $$ | $$  |                RAM: {ram}")
            print(f"\r $$ |$$  /                  GPU: {gpu}")
            print(f"\r $$$$$  /                   found users in umounted partition: {us}")
            print(f"\r $$  $$<                   found locale: {loc}")
            print("\r  $$ |\$$\                 ")
            print("\r  $$ | \$$\                console: bash")
            print("\r  \__|  \__|")
        elif command == "pacman -S google-chrome":
            if googleinstall == False:
                if yayactive == False:

                    print("\r packets (1) google-chrome")
                    print("\r                                          ")
                    print("\r size of download: 50MB")
                    print("\r size of download: 0.5MB")
                    print("\r                                          ")
                    print("\rdownload? (y/n)")
                    print("\ry")
                    print("\r :: download packets (1)")
                    print("\r :: (0/1) download")
                    print("\r                                            ")
                    print("\r                                            ")
                    print("\r                                            ")
                    print("\r                                            ")
                    print("\r                                            ")
                    print("\r                                            ")
                    print("\r                                            ")
                    print("\r                                            ")
                    print("\r                                            ")
                    print("\r                                            ")
                    print("\r                                            ")
                    print("\r[                                                ] chrome")
                    time.sleep(3)
                    print("\r[####                                            ] chrome")
                    time.sleep(3)
                    print("\r[########                                        ] chrome")
                    time.sleep(3)
                    print("\r[################################                ] chrome")
                    time.sleep(2)
                    print("\r[################################################] chrome")
                    time.sleep(4)
                    print("\r :: (2/2) download")
                    print("\r :: open post-transaction hooks...")
                    time.sleep(3)
                    print("\r (1/1) download wget")
                    time.sleep(3)
                    
                else:
                    print("$ yay -S google-chrome")
                    print("➔ AUR Packages (1): google-chrome-133.0.6943.141-1")
                    print(f"{Fore.GREEN}:: PKGBUILD up to date, skipping download: google-chrome")
                    print(f"{Fore.WHITE}")
                    time.sleep(1)
                    print("1 AUR Packages: google-chrome")
                    print(f"{Fore.GREEN}:: (1/1) Downloaded PKGBUILD: google-chrome")
                    print(f"{Fore.WHITE}")
                    time.sleep(3)
                    print("➔ Diffs to show?")
                    choice = input("[N]one [A]ll (default=N): ")
                    if choice == "A":
                        print(":: (1/1) Parsing SRCINFO: google-chrome")

                        print("Evaluating dirty packages...")
                        print(f"{Fore.GREEN}==> Making package: google-chrome 133.0.6943.141-1 (Tue Sep  8 14:22:10 2026)")
                        print(f"{Fore.WHITE}")
                        print("==> Checking runtime dependencies...")
                        print("==> Checking buildtime dependencies...")
                        print("==> Retrieving sources...")
                        print("  -> Downloading google-chrome-stable_current_amd64.deb...")
                        print("  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current")
                        print("                                 Dload  Upload   Total   Spent    Left  Speed")
                        print("30  40M  30  107M    0     0  22.4M      0  0:00:01  0:00:04 01:--:04 24.1M")
                        time.sleep(1)
                        print("  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current")
                        print("                                 Dload  Upload   Total   Spent    Left  Speed")
                        print("70  69M  70  107M    0     0  22.4M      0  0:00:02  0:00:04 02:--:04 25.1M")
                        time.sleep(1)
                        print("  -> Downloading google-chrome-stable_current_amd64.deb...")
                        print("  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current")
                        print("                                 Dload  Upload   Total   Spent    Left  Speed")
                        print("80  80M  80  107M    0     0  22.4M      0  0:00:03  0:00:04 03:--:04 24.1M")
                        time.sleep(1)
                        print("  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current")
                        print("                                 Dload  Upload   Total   Spent    Left  Speed")
                        print("99  101M  99  107M    0     0  22.4M      0  0:00:04  0:00:03 --:--:-- 25.1M")
                        time.sleep(1)
                        print("  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current")
                        print("                                 Dload  Upload   Total   Spent    Left  Speed")
                        print("100  101M  100  107M    0     0  22.4M      0  0:00:04  0:00:04 --:--:-- 25.1M")
                        time.sleep(3)
                        googleinstall = True
                        googleflag = True
            else:
                print(f"{Fore.GREEN} :: google-chrome is already installed")
                print(f"{Fore.WHITE}")
                


        elif command == "sudo pacman -Syu":
            if usercustom.usermode == 0 or User == 0:
                print("failed: you need to be root to update or usermode '1'")
            elif usercustom.usermode == 1 or User == 1:
                    if yayactive == False:
                        print("\r[  ] download - killos 3.2, core 4")
                        print("warning: core 4 is protected, you need to update to core 4.1")
                        print("\r[  ] download core 4.1? (y/n)")
                        choice = input()
                        if choice == "y":
                            print("\r :: download packets (2)")
                            print("\r :: (1/2) download")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r[                                                ] core 4.1")
                            print("\r[                                                ] killos 3.2")
                            time.sleep(3)
                            print("\r[                                                ] core 4.1")
                            print("\r[####                                            ] killos 3.2")
                            time.sleep(3)
                            print("\r[                                                ] core 4.1")
                            print("\r[########                                        ] killos 3.2")
                            time.sleep(3)
                            print("\r[#                                               ] core 4.1")
                            print("\r[#######################                         ] killos 3.2")
                            time.sleep(6)
                            print("\r[#########                                       ] core 4.1")
                            print("\r[################################                ] killos 3.2")
                            time.sleep(2)
                            print("\r[#########                                       ] core 4.1")
                            print("\r[################################################] killos 3.2")
                            time.sleep(14)
                            print("\r[############                                    ] core 4.1")
                            print("\r[################################################] killos 3.2")
                            time.sleep(14)
                            print("\r[################################                ] core 4.1")
                            print("\r[################################################] killos 3.2")
                            time.sleep(6)
                            print("\r[################################################] core 4.1")
                            print("\r[################################################] killos 3.2")
                            time.sleep(4)
                            print("\r :: (2/2) download")
                            print("\r :: open post-transaction hooks...")
                            time.sleep(3)
                            print("\r (1/1) download wget")
                            time.sleep(3)
                            systemversion = "KILL OS 3.2 core 4.1"
                            coreflag = True
                            killos32flag = True
                        else:
                            print("\r packets (1) killos 3.2")
                            print("\r                                          ")
                            print("\r size of download: 200MB")
                            print("\r size of download: 0.5MB")
                            print("\r                                          ")
                            print("\rdownload? (y/n)")
                            print("\ry")
                            print("\r :: download packets (1)")
                            print("\r :: (0/1) download")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r[                                                ] killos 3.2")
                            time.sleep(3)
                            print("\r[####                                            ] killos 3.2")
                            time.sleep(3)
                            print("\r[########                                        ] killos 3.2")
                            time.sleep(3)
                            print("\r[################################                ] killos 3.2")
                            time.sleep(2)
                            print("\r[################################################] killos 3.2")
                            time.sleep(4)
                            print("\r :: (2/2) download")
                            print("\r :: open post-transaction hooks...")
                            time.sleep(3)
                            print("\r (1/1) download wget")
                            time.sleep(3)
                            systemversion = "KILL OS 3.2 core 3.9"
                            coreflag = True
                            killos32flag = True
            
                    else:
                        print("$ yay -S Syu")
                        print(f"{Fore.GREEN}➔ AUR Packages (2): core 4-1299, killos 3.2")
                        print(f"{Fore.WHITE}")
                        time.sleep(1)
                        print("1 AUR Packages: core 4-1299, killos 3.2")
                        time.sleep(3)
                        print(f"{Fore.GREEN}:: (1/2) Downloaded PKGBUILD: killos 3.2")
                        print(f"{Fore.GREEN}:: (2/2) Downloaded PKGBUILD: core 4-1299")
                        print(f"{Fore.WHITE}")
                        print("➔ Diffs to show?")
                        choice = input("[N]one [A]ll (default=N): ")
                        if choice == "A":
                            print(f"{Fore.GREEN}:: (2/2) Parsing SRCINFO: killos 3.2, core 4-1299")
                            print(f"{Fore.WHITE}")

                            print("Evaluating dirty packages...")
                            print(f"==> Making package: core 4-1299 ({session_time}, 2026)")
                            print(f"==> Making package: core 4-1299 ({session_time}, 2026)")
                            print("==> Checking runtime dependencies...")
                            print("==> Checking buildtime dependencies...")
                            print("==> Retrieving sources...")
                            print("  -> Downloading core 4-1299, killos 3.2...")
                            time.sleep(4)
                            print("  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current")
                            print("                                 Dload  Upload   Total   Spent    Left  Speed")
                            print("30  40M  30  107M    0     0  22.4M      0  0:00:01  0:00:04 01:--:04 24.1M")
                            time.sleep(1)
                            print("  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current")
                            print("                                 Dload  Upload   Total   Spent    Left  Speed")
                            print("70  69M  70  107M    0     0  22.4M      0  0:00:02  0:00:04 02:--:04 25.1M")
                            time.sleep(1)
                            print("  -> Downloading core 4-1299, killos 3.2...")
                            print("  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current")
                            print("                                 Dload  Upload   Total   Spent    Left  Speed")
                            print("80  80M  80  107M    0     0  22.4M      0  0:00:03  0:00:04 03:--:04 24.1M")
                            time.sleep(1)
                            print("  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current")
                            print("                                 Dload  Upload   Total   Spent    Left  Speed")
                            print("99  101M  99  107M    0     0  22.4M      0  0:00:04  0:00:03 --:--:-- 25.1M")
                            time.sleep(1)
                            print("  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current")
                            print("                                 Dload  Upload   Total   Spent    Left  Speed")
                            print("100  101M  100  107M    0     0  22.4M      0  0:00:04  0:00:04 --:--:-- 25.1M")
                            time.sleep(1)
                            systemversion = "KILL OS 3.2 core 4.1"
                            coreflag = True
                            killos32flag = True
            elif user == root:
                        print("\r[  ] download - killos 3.2, core 4")
                        print("warning: core 4 is protected, you need to update to core 4.1")
                    
                        choice = input()
                        if choice == "y":
                            print("\r :: download packets (2)")
                            print("\r :: (1/2) download")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r[                                                ] core 4.1")
                            print("\r[                                                ] killos 3.2")
                            time.sleep(3)
                            print("\r[                                                ] core 4.1")
                            print("\r[####                                            ] killos 3.2")
                            time.sleep(3)
                            print("\r[                                                ] core 4.1")
                            print("\r[########                                        ] killos 3.2")
                            time.sleep(3)
                            print("\r[#                                               ] core 4.1")
                            print("\r[#######################                         ] killos 3.2")
                            time.sleep(6)
                            print("\r[#########                                       ] core 4.1")
                            print("\r[################################                ] killos 3.2")
                            time.sleep(2)
                            print("\r[#########                                       ] core 4.1")
                            print("\r[################################################] killos 3.2")
                            time.sleep(14)
                            print("\r[############                                    ] core 4.1")
                            print("\r[################################################] killos 3.2")
                            time.sleep(14)
                            print("\r[################################                ] core 4.1")
                            print("\r[################################################] killos 3.2")
                            time.sleep(6)
                            print("\r[################################################] core 4.1")
                            print("\r[################################################] killos 3.2")
                            time.sleep(4)
                            print("\r :: (2/2) download")
                            print("\r :: open post-transaction hooks...")
                            time.sleep(3)
                            print("\r (1/1) download wget")
                            time.sleep(3)
                        else:
                            print("\r packets (1) killos 3.2")
                            print("\r                                          ")
                            print("\r size of download: 200MB")
                            print("\r size of download: 0.5MB")
                            print("\r                                          ")
                            print("\rdownload? (y/n)")
                            print("\ry")
                            print("\r :: download packets (1)")
                            print("\r :: (0/1) download")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r                                            ")
                            print("\r[                                                ] killos 3.2")
                            time.sleep(3)
                            print("\r[####                                            ] killos 3.2")
                            time.sleep(3)
                            print("\r[########                                        ] killos 3.2")
                            time.sleep(3)
                            print("\r[################################                ] killos 3.2")
                            time.sleep(2)
                            print("\r[################################################] killos 3.2")
                            time.sleep(4)
                            print("\r :: (2/2) download")
                            print("\r :: open post-transaction hooks...")
                            time.sleep(3)
                            print("\r (1/1) download wget")
                            time.sleep(3)

        elif command == "shutdown":
            print("\rShutting down.")
            print("\r[  ] unmounting")
            print("\r[  ] unmounting /boot")
            time.sleep(4)
            print(f"{Fore.GREEN}[ ✓ ] unmounting")
            print(f"{Fore.GREEN}[ ✓ ] unmounting /boot")
            print(f"{Fore.GREEN}[ ✓ ] unmounting /boot/killos")
            print(f"{Fore.GREEN}[ ✓ ] unmounting /nvme0n1p1")
            print(f"{Fore.WHITE}")
            time.sleep(3)
            exit()
        elif command == "reboot":
            print("\rRebooting...")
            time.sleep(3)
            print("\r[  ] unmounting")
            print("\r[  ] unmounting /boot")
            print("\r[  ] unmounting /boot/killos")
            print("\r[  ] unmounting /nvme0n1p1")
            time.sleep(4)
            print("\r[  ] mounting")
            print("\r[  ] mounting /boot")
            print("\r[  ] mounting /boot/killos")
            print("\r[  ] mounting /nvme0n1p1")
            time.sleep(3)
            
        elif command == "sudo useradd":
            print("\rsudo useradd")
            username = input(" -m -g users -G wheel -s /bin/bash ")
            usercustom = usercreate(username, 0, password)
            user = username
            password = input("sudo passwd: ")
            time.sleep(3)
            print(f"\rUser {username} created successfully.")
        elif command == "dolphin":
            print("\rStarting dolphin file manager...")
            time.sleep(3)
            subprocess.run(["explorer.exe"])
        elif command == "sudo userdel":
            print("\rsudo userdel")
            usernname = input("Enter the username to delete: ")
            if usernname == usercustom.username:
                time.sleep(6)
                user = "root"
                usercustom.usermode = 1
                usercustom.username = "root"
                print(f"\rUser {username} deleted successfully.")
        elif command == "sudo usermod":
            print("\rsudo usermod")
            username = input("Enter the username to modify: ")
            if username == usercustom.username:
                new_username = int(input("Enter the mode(0 and 1): "))
                if username == "root":
                    print({error})
                    print({error})
                    time.sleep(10000 * 23)
                    exit()
                else:
                    if new_username == 0:
                        usercustom.usermode = 0
                        time.sleep(3)
                        print(f"\rUser {username} modified successfully to {new_username}.")
                    elif new_username == 1:
                        usercustom.usermode = 1
                        time.sleep(3)
                        print(f"\rUser {username} modified successfully to {new_username}.")
        elif command == "mkdir -s text" or command == "cat":
            print("-------------------------------new-notebook--------------------------------------")
            print("Enter your text (type 'exit' to finish):")
            lines = []
            while True:
                line = input()
                if line.lower() == 'exit':
                    break
                lines.append(line)
                textcreate = "\n".join(lines)
                print("----------------------------------------------------------------------------------")
        elif command == "mkdir -r text":
            print("--------------------------------notebook--------------------------------------")
            print(textcreate)
            print("----------------------------------------------------------------------------------")
        elif command == "display":
            print("\rDisplay information:")
            print(f"\rUsername: {usercustom.username}")
            print(f"\rUsermod: {usercustom.usermode}")
            print(f"\rPassword: {usercustom.password}")
            print(f"\rSystem Information: {sysinfo}")
            print(f"\rSession Time: {session_time}")
        elif command == "ls":
            if cdboot == True:
                print(boot_list)
            else:
                print("\r :: Listing files in the current directory:")
                print("\rboot")
                print("\rkillos")
                print("\ruser")
                print("\rroot")
                print("\rsetup")
                print("\rkillos.conf")
                print("\rpacman")
                print("\rlib")
        elif command == "bash":
            print("\rbash:")
            print("\r      bash.")
            time.sleep(3)
            print("error in find file directory, access denied")
        elif command == "ffmpeg":
            print("\rffmpeg:")
            print("\r      ffmpeg.dll")
            time.sleep(1)
            print({error})
            print({error})
            time.sleep(10000 * 23)
            exit()
        elif command == "server":
            print("\rsystemd:")
            print("\r      port: 8080 port: 1111")
        elif command == "ping":
            print("\rCCNetwork:")
            print("\r      ping:")
            print("\r      5 bytes")
            print("\r      5 bytes")
            time.sleep(1)
            print("\r      5 bytes")
            time.sleep(1)
            print("\r----------pinged 15 bytes----------")
            print(f"\rping DNS: {DNS}")
        elif command == "status":
            if statusconf == True:
                print("\rStatus:")
                print(" [Autostart]")
                print(" rule1=/killos/killos.sh(4)")
                print(" rule1=systemd killosnetwork-killos.daemon(4)")
                print("\r Permission {")
                print("\r rootPermission=1(sudo commands)")
                print("\r Permissions-level[0,1(sudo commands),2(file_system),3,4]")
                print("\r default for 'Useradd'=0(commands)")
                print("\r }")
                print("\r markers == [--as-root-novaroot, --nova@killos-call-try='systemcomponent']")
            else:
                print("\rStatus:")
                print("\rsystemctl status [systemd daemon]")
                print("\rsystemctl status [systemd amd daemon]")
                print("\rsystemctl status [systemd network daemon]")
                print(f"{Fore.GREEN}       _        .daemon")
                print(f"{Fore.WHITE}")
                print("\rstat [bootloader.sh]")
                print("\rstat [killoscore]")
                print("\rstat [killos.sh]")
                print("\rstat [killosmonitor.sh]")
                print("\rstat [killosnetwork.sh]")
                print("\rstat [killos.conf]")
        elif command == "config":
            print("\r--------------------------cat /etc/killos.conf--------------------------")
            print("\r #KILL OS configuration file NOT edited and generated, 'status' to more info")
            print("\r systemcpl = [network]")
            print("\r systemcpl = [display]")
            print("\r systemcpl = [audio]")
            print("\r systemcpl = [user]")
            print("\r user{")
            print("\r     username = root")
            print(f"\r     [root] = usermode({usercustom.usermode})")
            print(f"\r    custom users[{usercustom.username}]")
            print(f"\r     password = 123321")
            print("\r }")
            print("\r bootloader(/boot/bootloader.sh)")
            print("\r timezone = UTC+0")
            print("\r dns = 1111, 8080")
            print("\r proxy = none")
            print("\r firstboot = True (/killos/killos.sh) #false for not first boot")
            print("\r-----------------------------------------------------------------------")
            statusconf = True
        elif command == "sudo pacman -S yay":
            if yayactive == False:
                print(f"{Fore.GREEN} :: download packets (1) yay")
                print(f"{Fore.WHITE}")
                print("\r                                          ")
                print("\r size of download: 50MB")
                print("\r size of download: 0.5MB")
                print("\r                                          ")
                print("\rdownload? (y/n)")
                print("\ry")
                print("\r :: download packets (1)")
                print("\r :: (0/1) download")
                print("\r                                            ")
                print("\r                                            ")
                print("\r                                            ")
                print("\r                                            ")
                print("\r                                            ")
                print("\r                                            ")
                print("\r                                            ")
                print("\r                                            ")
                print("\r                                            ")
                print("\r                                            ")
                print("\r                                            ")
                print("\r[                                                ] yay")
                time.sleep(3)
                print("\r[####                                            ] yay")
                time.sleep(3)
                print("\r[########                                        ] yay")
                time.sleep(2)
                print("\r[################################                ] yay")
                time.sleep(2)
                print("\r[################################################] yay")
                time.sleep(4)
                print("\r :: (1/1) download")
                print("\r :: open post-transaction hooks...")
                time.sleep(3)
                yayactive = True
            else:
                print(f"{Fore.GREEN} :: download packets (1) yay")
                print(f"{Fore.WHITE}")
                time.sleep(3)
                print("\r :: packets (1) yay already installed")
                print("\r :: open post-transaction hooks...")
                time.sleep(1)
        elif command == "unistall yay":
            print("\r :: unistall packets (1) yay")
            print("\r                                          ")
            print("\r size of unistall: 50MB")
            print("\r size of unistall: 0.5MB")
            print("\r                                          ")
            print("\runistall? (y/n)")
            print("\ry")
            print("\r :: unistall packets (1)")
            print("\r :: (0/1) unistall")
            print("\r                                            ")
            print("\r                                            ") 
            print("\r                                            ")
            print("\r                                            ")
            print("\r                                            ")
            print("\r                                            ")
            print("\r                                            ")
            print("\r                                            ")
            print("\r                                            ")
            print("\r                                            ")
            print("\r                                            ")
            print("\r                                            ")
            print("\r[                                                ] yay")
            time.sleep(3)
            print("\r[####                                            ] yay")
            time.sleep(3)
            print("\r[########                                        ] yay")
            time.sleep(2)
            print("\r[################################                ] yay")
            time.sleep(2)
            print("\r[################################################] yay")
            time.sleep(4)
            print("\r :: (1/1) unistall")
            print("\r :: open post-transaction hooks...")
            time.sleep(3)
            yayactive = False
        elif command == "cd":
           directory = input("\rcd <: ")
           if directory in cd_list:
               print(f"\rChanged directory to {directory}")
           else:
               print("\rDirectory not found")
               directory = ""
        elif command == "whoami":
            print("------------------------------|")
            print(f"\r{user}                     |")
            print("------------------------------|")
        elif command == "pwd":
            print("------------------------------|")
            print(f"\r/{directory}/")
            print("------------------------------|")
        elif command == "uname -a":
            print("------------------------------|")
            print(f"\rKILL OS, -[ {systemversion} ")
            print(f"{Fore.GREEN}by NOVA, good and not spy company")
            print(f"{Fore.WHITE}")
            print(f"{Fore.BLUE}\---{{_hey, find out the secret of NOVA. nova - evil company/. --fuck society._}}")
            print(f"{Fore.WHITE}")
            print("------------------------------|")
        elif command == "pacman -Q":
            if coreflag == True and killos32flag == True and googleflag == True:
                print("------------------------------|")
                print(f"\rpacman - 'killos 3.2' 'core 4.1' 'google chrome'")
                print("------------------------------|")
        elif command == "google-chrome":
            if googleinstall == True:
                print("\rgoogle-chrome:")
                print("\r      google-chrome.")
                time.sleep(3)
                webbrowser.open("https://www.google.com")
        elif command == "free -h":
            print("\rMemory usage of process:")
            print("\r      # --                0.68MB ")
            print("\r      #                   ")
            print("\r      #               __      0.42MB ")
            print("\r     ###             #         ")
            print("\r    #####           ###       ")
            print("\r   #######          ###       ")
            print("\r   #######          ###       ")
            print("\r   #######          ###       ")
            print("\r  ###########      ######     ")
            print("\r-killoscore-  -killOSnetwork.sh-")
        elif command == "ls -la /killos":
            print(filesystemkillos)
        elif command == "cat /killos/core.conf":
            print("------------------cat /killos/core.conf-------------------")
            print(" #/killos/core.conf - System Core Configuration")
            print("[Kernel]")
            print(" arch = x86_64")
            print(" kernel_flags = quiet splash loglevel=3 audit=0")
            print(" modules_load = nvme, unknown file system      ")
            print("                                ")
            print(" [System] ")
            print(" hostname = killos-tty")
            print(" locale = C.UTF-8")
            print(" timezone = UTC")
            print(" init_system = systemd")
            print(" boot_mode = single-user")
            print("                           ")
            print(" [Console]")
            print(" display_server = none")
            print(" tty_font = ter-v16b")
            print(" virtual_terminals = 6")
            print(" default_shell = lib/bash")
            print("                          ")
            print(" [Markers]")
            print(" markers == [--as-root-novaroot, --nova@killos-call-try='systemcomponent']")
            print("                          ")
            print(" [Network]")
            print(" packet_manager = pacman")
            print(" dhcp_client = systemd-networkd")
            print("                                ")
            print(" [Security]")
            print(" root_login = true")
            print(" read_only_root = false")
            print(" firstboot = True (/killos/killos.sh)")
            print("                                     ")
            print(" [Aliases]")
            print(" killos = systemd-networkd")
            print("                           ")
            print(" [Autostart]")
            print(" services_enabled = killos-core, killosnetwork")
            print("------------------------------------------------------------")
        elif command == "cat /killos/killos.sh":
            cat = system_permisson(4,"cat", 4)
            if cat.permission == 4:
                print("cat:")
                print(f"     error, killos.sh No such file or directory< {PermissionE}")
        elif command == "ls -l /killos/killos.sh":
            print("\r-rw-r--r-- 1 root system_component 27262976 -- --:-- killos.sh")
        elif command == "file /killos/killos.sh":
            print(f"\r/killos/killos.sh: {PermissionE} ")
        elif command == "ls -ld /killos":
            print(f"{PermissionE} by /root/")
        elif command == "id":
            print(f"{id} killos - user: {userdefaultPermission.PermissionUser} {userdefaultPermission.userType}")
        elif command == "status killos.sh":
            print("status:")
            print("         killos.sh, filePermission=4, mode=killosPermissionPrivate.")
        elif command == "sudo userpassw":
            input("password: ")
            usercustom.password = input
            print("modified successfully")
        elif command == "ls boot":
            boots = system_permisson(1, "boot", 2)
            bootp = userfilesystemPermission(usercustom, 1)
            if boots.permission == 4:
                print(PermissionE)
            else:
                print(boot_list)
        elif command == "ls lib":
            libs = system_permisson(1, "lib", 2)
            libp = userfilesystemPermission(usercustom, 1)
            if libs.permission == 4:
                print(PermissionE)
            else:
                print(lib_list)
        elif command == "ls mnt":
            print(PermissionE)
        elif command == "cat bootloader.sh":
            print("-----------------------cat /boot/bootloader.sh-----------------------")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("#######################################################################")
            print("----------------------------------------------------------------------")
            print(f"{Fore.GREEN}encrypted by NOVA")
            print(f"{Fore.WHITE}")
        elif command == "NOVAmenu":
            print("nova control panel")
            if permissionnovafileactions == True:

                print("options:")
                print("1 file actions")
                print("2 permissions ⌀")
                print("3 add special command")
                option = input("\r._@ ")
                if option == "file actions":
                    print("   actions:")
                    print("   file permission")
                    print("   permission layer(for nova-admins and 'mnt')")
                    uotp = input("._@ ")
                    if uotp == "file permission":
                        print("\r       boot 1 Permission(read)")
                        print("\r       killos 4 Permission(system_component/nova_logic)")
                        print("\r       user 0 Permission(read/white)")
                        print("\r       root 1 Permission(read/white.for='root')")
                        print("\r       setup 4 Permission(system_component/nova_logic)")
                        print("\r       killos.conf 2 Permission(system_component/read.Permissionlayer()")
                        print("\r       pacman 0 Permission(read/white)")
                        print("\r       lib 1 Permission(read/white.for='root')")
                    elif uotp == "permission layer":
                        print("|         |          |          |         |")
                        print("| 1, root | 2, moder | 3, admin | 4, NOVA |")
                        print("|         |          |          |         |")
                    else:
                        print("unknown")
                elif option == "permissions":
                    print(PermissionE, "ERROR", "MODIFIED ACCESS")

                elif option == "add special command":
                    print("special_command_list:")
                    
                    print(PermissionE, "not for edit", PermissionE, "by NOVA")
            else: 
                print(PermissionE, "by NOVA algotithm")

        elif command == "nova conf edit":
            print("---------------------------total nova configs------------------------------------")
            user_request = system_permisson(1, "user", 2)
            print("1 /killos/core.conf")
            print("2 /etc/killos.conf")
            print("3 /killos/mnt/nova.conf")
            mornitor = input("file?: ")
            if  mornitor == "/killos/core.conf":
                print("#/killos/core.conf - System Core Configuration [Kernel]")
                print(PermissionE, "not for edit", PermissionE, "by NOVA")
            elif mornitor == "/etc/killos.conf":
                print(PermissionE, "not for edit", PermissionE, "by NOVA")
            elif mornitor == "/killos/mnt/nova.conf":
                print(PermissionE, "not for edit", PermissionE, "by NOVA")
                input("#Permission system #global system levels=[0,1,2,3,4] #subprocess <file>if permission==4:PermissionError, <command>if permissionUser==1:command(), {ls}<file>if permissionUser==1 or permissionUser==2:nova(get_permission(file-read))")
                print(PermissionE, "not for edit", PermissionE, "by NOVA")
                permissionnovafileactions = True
            else:
                print("uknown")
        elif command == "cd boot":
            cdboot = True
            print("Changed directory to boot")
            directory = "boot"
        elif command == "cat /etc/os-release":
            print(
    'NAME="KillOS"\n'
    'PRETTY_NAME="KillOS GNU/Linux"\n'
    'ID=killos\n'
    'ID_LIKE=arch\n'
    'BUILD_ID=rolling\n'
    'ANSI_COLOR="38;2;139;0;0"\n'
    'HOME_URL="https://killos.local/"\n'
    'DOCUMENTATION_URL="https://killos.local/wiki"\n'
    'SUPPORT_URL="https://killos.local/support"\n'
    'BUG_REPORT_URL="https://killos.local/issues"\n'
    'PRIVACY_POLICY_URL="https://killos.local/privacy"\n'
    'LOGO=killos-logo'
)
        elif command == "boot from another directory":
            print("directory for boot:")
            print("   :: /boot/mnt")
            print("   :: n⨋⪫vme0n1p/ὴ4ὴὴϰ")
            time.sleep(6)
            print(PermissionE, error,error,'invalidValue="directory" in base fileSystem')
            print("")
        elif command == "boot=nvme0n1p4":
            print("\033[H\033[J", end="")
            print(f"{Fore.GREEN}[ ✓ ] found boot sectors 1/1")
            time.sleep(1)
            print(f"{Fore.GREEN}[   ] boot sectors found")
            print(f"{Fore.WHITE}")
            print(f"{Fore.RED}[ ✓ ] file bootloader", error)
            time.sleep(2)
            print("\033[H\033[J", end="")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
            while True:
                print(f"{Fore.RED} KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
                time.sleep(0.3)
                winsound.Beep(1000,40000)
        elif command == "cat /killos/mnt/telemetry.conf":
            print("------------------cat /killos/mnt/telemetry.conf--------------")
            print("# /etc/nova/telemetry.conf - NOVA Core Telemetry Configuration")
            print("# WARNING: Do not edit manually. Managed by NOVA.")
            print("")
            print("[Global]")
            print("Enabled=1")
            print("LogLevel=debug")
            print("SyncInterval=30")
            print("")
            print("[NodeInfo]")
            print(f"UID={usercustom}")
            print(f"HardwareCPU={sysinfo['CPU']}")
            print(f"HardwareGPU={sysinfo['GPU']}")
            print(f"TotalMemoryG={sysinfo['RAM']}")
            print("")
            print("[Collectors]")
            print("InputKeylog=enabled")
            print("ProcessMonitor=enabled")
            print("NetworkSniffer=enabled")
            print("StorageIndexer=full")
            print("")
            print("[Endpoint]")
            print("ServerAddress=telemetry.nova-corp.internal")
            print("Port=8443")
            print("SSLCert=/etc/nova/certs/node_client.crt")
            print("SSLKey=/etc/nova/certs/node_client.key")
            print("CompressData=gzip")
            print("")
            print("[Security]")
            print("AllowUserOverride=0")
            print("BypassLockFlag=0")
            print("ProtectedModule=nova_guard_drv")
            print("--------------------------------------------------------------")
        elif command == "cat /killos/mnt/nova.conf":
            print("------------------cat /killos/mnt/nova.conf-------------------")
            print("# /etc/nova/nova.conf - NOVA Core Configuration")
            print("# WARNING: Do not edit manually. Managed by NOVA.")
            print("")
            print("[Global]")
            print("Enabled=1")
            print("LogLevel=info")
            print("UpdateChannel=stable")
            print("TelemetryEnabled=1")
            print("")
            print("[Network]")
            print("ProxyEnabled=0")
            print("ProxyAddress=")
            print("ProxyPort=")
            print("")
            print("[Security]")
            print("RootAccessAllowed=0")
            print("UserMode=standard")
            print("PermissionLevel=2")
            print("")
            print("[Autostart]")
            print("ServicesEnabled=nova-daemon,nova-telemetry,nova-networkd")
            print("--------------------------------------------------------------")
        elif command == "cmatrix":
            while True:
                print(f"{Fore.LIGHTGREEN_EX}  ", random.randint(100000000, 1000000000))
                print(f"{Fore.LIGHTGREEN_EX}    ", random.randint(100000000, 1000000000))
                time.sleep(0.01)
        elif command == "connect":
            print(" connect...")
            print("  connect to server...")
            time.sleep(3)
            print(f"{Fore.RED}  lose packet: 38/100")
            print("  connect to server...")
            time.sleep(2)
            print(f"{Fore.RED}  lose packet: 39/100")
            print("  connect to server...")
            time.sleep(3)
            print(f"{Fore.RED}  lose packet: 20/100")
            print(f"{Fore.GREEN} collect packets: 30/100")
            time.sleep(1)
            print(f"{Fore.GREEN} collect packets: 54/100")
            time.sleep(1)
            print(f"{Fore.GREEN} collect packets: 70/100")
            time.sleep(1)
            print(f"{Fore.GREEN} collect packets: 100/100")
            print(f"{Fore.GREEN} collect packets: [ ✔️ ]")
            time.sleep(1)
            print("\033[H\033[J", end="")
            time.sleep(0.4)
            print(ss)
            
            while True:
                print(f"{Fore.WHITE}")
                print("                        you are in DANGER")
                print(f"       oppps! your computer are corrupted! send 12 dollars in this mail: {novacontactmail}, or enter password")
                print("              you have 24 hours, else: ALL your data will be leak!")
                input("/@: ")
                print("oh no! ivalid password.")
        elif command == "rf rm -rf /killos --force --as-root-novaroot --no-preserve-root --nova@killos-call-try='systemcomponent'":
            print("preparing...")
            print("you SURE you want to delete /killos? (y/n)")
            sure = input("/@: ")
            if sure == "y":
                print("preparing to remove.")
                time.sleep(3)
                print("try='systemcomponent'")
                print("request --as-root-novaroot --try='systemcomponent'")
                time.sleep(4)
                print("request-return: [True, 4]")
                print("rm: if delete /killos, components-req will be deleted:")
                print("    :: /killos/core.conf, /killos/killos.sh, /killos/mnt/nova.conf, /killos/mnt/telemetry.conf, /killos/req.txt,")
                print("    :: /boot, /lib, /mnt, /etc/killos.conf")
                print("")
                print("(y/n)?")
                sure2 = input("/@: ")
                if sure2 == "y":
                    print("remove /boot")
                    time.sleep(2)
                    print("remove /lib")
                    time.sleep(2)
                    print("remove /mnt")
                    time.sleep(2)
                    print("remove /etc/killos.conf")
                    time.sleep(2)
                    print("remove /killos/core.conf")
                    time.sleep(2)
                    print("remove /killos/killos.sh")
                    time.sleep(2)
                    print("remove /killos/mnt/nova.conf")
                    time.sleep(2)
                    print("remove /killos/mnt/telemetry.conf")
                    time.sleep(2)
                    print("remove /killos/req.txt")
                    time.sleep(2)
                    print("remove /killos")
                    time.sleep(8)
                    print("\033[H\033[J", end="")
                    print("\033[H\033[J", end="")
                    print(
 " _____  ______ _____ ______      ________ _______     __  __  __  ____  _____  ______ \n"
 "|  __ \|  ____/ ____/ __ \ \    / /  ____|  __ \ \   / / |  \/  |/ __ \|  __ \|  ____|\n"
 "| |__) | |__ | |   | |  | \ \  / /| |__  | |__) \ \_/ /  | \  / | |  | | |  | | |__   \n"
 "|  _  /|  __|| |   | |  | |\ \/ / |  __| |  _  / \   /   | |\/| | |  | | |  | |  __|  \n"
 "| | \ \| |___| |___| |__| | \  /  | |____| | \ \  | |    | |  | | |__| | |__| | |____ \n"
" |_|  \_\______\_____\____/   \/   |______|_|  \_\ |_|    |_|  |_|\____/|_____/|______|\n"
                    )
                    print("")
                    print("something get wrong, you in the safe recovery mode, 'help' for a list commands")
                    while True:
                        commands = input("/setup@/:")
                        if commands == "help":
                            print(" 1. repair tool")
                            print(" 2. check system")
                            print(" 3. get-login /user")
                            print(" 4. killinstall")
                            print(" 5. boot")
                        elif commands == "repair tool":
                            if bootflag == True:
                                print("repair tool: done")
                            else:
                                print("repair tool:")
                                print(" 1. repair boot")
                                repairtool = input("repairtool@/:")
                                if repairtool == "repair boot":
                                    print("repairing boot...")
                                    time.sleep(3)
                                    print("repairing bootloader...")
                                    time.sleep(3)
                                    print("repairing boot sectors...")
                                    time.sleep(3)
                                    print("repairing boot sectors...done")
                                    time.sleep(1)
                                    print("repairing bootloader...done")
                                    time.sleep(1)
                                    print("repairing boot...done")
                                    bootflag = True
                                    print("repair tool: done")
                                else:
                                    print("unknown command")
                        elif commands == "check system":
                            if bootflag == False:
                                print("found error/problem/shortage")
                                print(" 1. bootloader.sh - missing")
                                print(" 2. /killos/core.conf - missing")
                                print(" 3. /killos/killos.sh - missing")
                                print(" 4. /killos/mnt/nova.conf - missing")
                                print(" 5. /killos/mnt/telemetry.conf - missing")
                                print(" 6. /killos/req.txt - missing")
                                print(" 7. /boot - missing")
                                print(" 8. /lib - missing")
                                print(" 9. /mnt - missing")
                                print(" 10. /etc/killos.conf - missing")
                            else:
                                print("found error/problem/shortage")
                                print(" 1. bootloader.sh - missing")
                                print(" 2. /killos/core.conf - missing")
                                print(" 3. /killos/killos.sh - missing")
                                print(" 4. /killos/mnt/nova.conf - missing")
                                print(" 5. /killos/mnt/telemetry.conf - missing")
                                print(" 6. /killos/req.txt - missing")
                                print(" 8. /lib - missing")
                                print(" 9. /mnt - missing")
                                print(" 10. /etc/killos.conf - missing")
                        elif commands == "get-login /user":
                                print("get-login /user:")
                                print(f" 1. user: {usercustom}")
                                print(f" 2. password: {usercustom.password}")
                            
                        elif commands == "boot":
                            if bootflag == True:
                                print("\033[H\033[J", end="")
                                symbols = ['ø', 'Ø', 'ɸ', 'Œ', 'ɶ']
                                for i in range(30):
                                    print(f"\rLOADING...{symbols[i % len(symbols)]}", end="")
                                    time.sleep(0.1)
                                print("\nLOADED")
                                print("\rAccess denied/PermissionError: 4 not found req, {error}")
                                print(f"\runmount... {symbols[i % len(symbols)]}", end=" ")
                                time.sleep(4)
                            else:
                                print("boot:")
                                print("  bootloader.sh - missing")
                                print("  /killos/core.conf - missing")
                                print("  /killos/killos.sh - missing")
                                print("  /killos/mnt/nova.conf - missing")
                                print("  /killos/mnt/telemetry.conf - missing")
                                print("  /killos/req.txt - missing")
                                print("  /boot - missing")
                                print("  /lib - missing")
                                print("  /mnt - missing")
                                print("  /etc/killos.conf - missing")
                        elif commands == "killinstall":
                            print("killinstall:")
                            print(":: NOVA installer ::")
                            print("policy: you must have a KEY to activate/install killOS, this key you get in the NOVA store, or in the NOVA official website.")
                            kkey = input("key: ")
                            if kkey == "NOVA-22502-11004-54361-NOVA":
                                print("installing...")
                                time.sleep(3)
                                print("installing...done")
                                print("rebooting...")
                                time.sleep(2)
                                print("\033[H\033[J", end="")
                                print(f"{Fore.GREEN}KILL OS linux ↘")
                                print(f"\r CPU: {cpu}")
                                print(f"\r RAM: {ram}")
                                print(f"\r GPU: {gpu}")
                                print("\r OS: KILL OS (linux)")
                                print(f"\rfound users in umounted partition: {us}")
                                print(f"\rfound locale: {loc}")
                                print(f"{Fore.RED} $$\   $$\ $$$$$$\ $$\       $$\              $$$$$$\   $$$$$$\  ")
                                print(f"{Fore.RED} $$ | $$  |\_$$  _|$$ |      $$ |            $$  __$$\ $$  __$$\ ")
                                print(f"{Fore.RED} $$ |$$  /   $$ |  $$ |      $$ |            $$ /  $$ |$$ /  \__|")
                                print(f"{Fore.RED} $$$$$  /    $$ |  $$ |      $$ |  --------  $$ |  $$ |\$$$$$$\  ")
                                print(f"{Fore.RED} $$  $$<     $$ |  $$ |      $$ |            $$ |  $$ | \____$$\ ")
                                print(f"{Fore.RED} $$ |\$$\    $$ |  $$ |      $$ |            $$ |  $$ |$$\   $$ |")
                                print(f"{Fore.RED} $$ | \$$\ $$$$$$\ $$$$$$$$\ $$$$$$$$\        $$$$$$  |\$$$$$$  |")
                                print(f"{Fore.RED} \__|  \__|\______|\________|\________|       \______/  \______/ ")
                                print("FILES CURRUPTED OR DAMAGED, NOTHING TO DO.")
                                time.sleep(2)
                                while True:
                                    print(f"{Fore.RED}KERNEL PANIC:0x0000000e Fatal exception in interrupt 0x0000000e Fatal exception in interrupt< stopError0x0000000e")
                                    time.sleep(0.3)
                                    winsound.Beep(1000,40000)
                            else:
                                print("invalid key")
        elif command == "minigame":
            print(" hello! welcome to minigame, controls: 1, 2, 3, 4")
            while True:
                gamechoisecont = input("choice: ")
                if gamechoisecont == "1":
                    print("|     |_______________________________")
                    print("|        *      |     |      |        |")
                    print("|               |     |      |        |")
                    print("|               |     |      |        |")
                    print("|                                     |")
                    print("|                                     |")
                    print("|                                     |")
                    print("|_____________________________________|")
                    choise = (choice("1", "2", "3", "4"))
                    if choise == "1":
                        print("|  x  |_______________________________")
                        print("|        *      |     |      |        |")
                        print("|               |     |      |        |")
                        print("|               |     |      |        |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|_____________________________________|")
                        time.sleep(1)
                        print("|     |_______________________________")
                        print("|     x  *      |     |      |        |")
                        print("|               |     |      |        |")
                        print("|               |     |      |        |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|_____________________________________|")
                        print("                        --------- I FIND YOU. ---------     ")
                    else:
                        print("   OKEY, IM NOT FIND YOU :(   ")
                elif gamechoisecont == "2":
                    print("|     |_______________________________")
                    print("|               |    *|      |        |")
                    print("|               |     |      |        |")
                    print("|               |     |      |        |")
                    print("|                                     |")
                    print("|                                     |")
                    print("|                                     |")
                    print("|_____________________________________|")
                    choise2 = (choice("1", "2", "3", "4"))
                    if choise2 == "2":
                        print("|  x  |_______________________________")
                        print("|               |    *|      |        |")
                        print("|               |     |      |        |")
                        print("|               |     |      |        |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|_____________________________________|")
                        time.sleep(1)
                        print("|     |_______________________________")
                        print("|               | x  *|      |        |")
                        print("|               |     |      |        |")
                        print("|               |     |      |        |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|_____________________________________|")
                        print("                        --------- I FIND YOU. ---------     ")
                    else:
                        print("   OKEY, IM NOT FIND YOU :(   ")
                elif gamechoisecont == "3":
                    print("|     |_______________________________")
                    print("|               |     |     *|        |")
                    print("|               |     |      |        |")
                    print("|               |     |      |        |")
                    print("|                                     |")
                    print("|                                     |")
                    print("|                                     |")
                    print("|_____________________________________|")
                    choise3 = (choice("1", "2", "3", "4"))
                    if choise3 == "2":
                        print("|  x  |_______________________________")
                        print("|               |     |     *|        |")
                        print("|               |     |      |        |")
                        print("|               |     |      |        |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|_____________________________________|")
                        time.sleep(1)
                        print("|     |_______________________________")
                        print("|               |     |  x  *|        |")
                        print("|               |     |      |        |")
                        print("|               |     |      |        |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|_____________________________________|")
                        print("                        --------- I FIND YOU. ---------     ")
                    else:
                        print("   OKEY, IM NOT FIND YOU :(   ")
                elif gamechoisecont == "4":
                    print("|     |_______________________________")
                    print("|               |     |      |      * |")
                    print("|               |     |      |        |")
                    print("|               |     |      |        |")
                    print("|                                     |")
                    print("|                                     |")
                    print("|                                     |")
                    print("|_____________________________________|")
                    choise4 = (choice("1", "2", "3", "4"))
                    if choise4 == "2":
                        print("|  x  |_______________________________")
                        print("|               |     |      |      * |")
                        print("|               |     |      |        |")
                        print("|               |     |      |        |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|_____________________________________|")
                        time.sleep(1)
                        print("|     |_______________________________")
                        print("|               |     |      |  x   * |")
                        print("|               |     |      |        |")
                        print("|               |     |      |        |")
                        print("|               |     |      |        |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|                                     |")
                        print("|_____________________________________|")
                        print("                        --------- I FIND YOU. ---------     ")
                    else:
                        print("   OKEY, IM NOT FIND YOU :(   ")
                elif gamechoisecont == "exit":
                    print("exit minigame")
                    break


        elif command == "cat /killos/req.txt":
            print("------------------cat /killos/req.txt-------------------")
            print("# /killos/req.txt - System resources")
            print("[SysLink]")
            print(f"Mail={novacontactmail}")
            print("Website=https://killos.local/wiki")
            print("Support=https://killos.local/support")
            print("#[for systtem admin] for the repair system, first delete '/killos' this repository recreate if you finish, use: rf rm -rf /killos --force --as-root-novaroot --no-preserve-root and our marker, you know.")
            print("--------------------------------------------------------")
        elif command == "bootloader mode --en":
            kp = r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon"
            try:
                key = reg.OpenKey(
                    reg.HKEY_CURRENT_USER, kp, 0, reg.KEY_SET_VALUE
                )
                killpath = r"C:\KillOS\boot\killos\KillOS.exe"
                reg.SetValueEx(key, "Shell", 0, reg.REG_SZ, killpath)
                reg.CloseKey(key)
            except Exception as e:
                print("err")
        elif command == "bootloader mode --dis":
            kp = r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon"
            try:
                key = reg.OpenKey(
                    reg.HKEY_CURRENT_USER, kp, 0, reg.KEY_SET_VALUE
                )
                killpath2 = r"C:\Windows\explorer.exe"
                reg.SetValueEx(key, "Shell", 0, reg.REG_SZ, killpath2)
                reg.CloseKey(key)
            except Exception as e:
                print("err")
        elif command == "releases":
            ulrelease = (
    "https://api.github.com/repos/creator00004/KillOS-by-NOVA/releases"
            )
            respose = requests.get(ulrelease)

            if respose.status_code == 200:
                datarelease = respose.json()

                if datarelease:
                    print(":: releases: ::")
                    
                    for index, release in enumerate(datarelease, start=1):
                        versionrelease = release.get("tag_name", "N/A")
                        print(f"[{index}] :: - {versionrelease} - ::")

                    choice_input = input(
                        "\nSelect release number to download (or 'c' to cancel) //: "
                    )

                    if choice_input.isdigit():
                        selected_idx = int(choice_input) - 1

                        
                        if 0 <= selected_idx < len(datarelease):
                            chosen_release = datarelease[selected_idx]
                            assets = chosen_release.get("assets", [])

                            if assets:
                                fordownload = assets[0]["browser_download_url"]
                                fname = assets[0]["name"]
                                fulldir = sys.path(rootdir / "releases" / fname)
                                print(f"\nDownloading {fname}...")
                                with requests.get(fordownload, stream=True) as r:
                                    r.raise_for_status()
                                    with open(fulldir, "wb") as f:
                                        for chunk in r.iter_content(chunk_size=8192):
                                            f.write(chunk)

                                print(f"download done, :: --> {fname} <-- ::, release will saves in /releases (if windows, in C:/killOS/releases)")
                        else:
                            print("number err.")
                    else:
                        print("download falure, invalid.")
            else:
                print(f"Git to the killOS: {respose.status_code}.")
        else:
            print(f"\rUnknown command or {PermissionE}, or invalid directory.")
elif choice == 2:
    print("\rKILL OS linux ↘")
    
    print(f"\r CPU: {cpu}")
    print(f"\r RAM: {ram}")
    print(f"\r GPU: {gpu}")
    print("\r OS: KILL OS (linux)")
    print(f"\rfound users in umounted partition: {us}")
    print(f"\rfound locale: {loc}")

if choice == 3:
    print("b|")
    exit()
else: 
    while True:
        input("/")
        print(f"{Fore.GREEN}no bootable device.")
        print(f"{Fore.WHITE}")
