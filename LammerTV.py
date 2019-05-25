#AmirAlisardar
#v 1.1
import os
import urllib
ip = urllib.urlopen("http://ip.42.pl/raw").read()

os.system("clrar")
os.system("clear")
os.system("clear")
os.system("figlet LammerTV | lolcat")
os.system("figlet FrameWork | lolcat")
print'''

\033[1;32m
                Create By AmirCyber01
==================================================== 
[+]  Team       : LammerTV
[+]  Programmer : AmirCyber01 ;)         
[+]  Github     : https://github.com/AmirCyber01                                                             
[+]  Instagram  : https://instagram.com/Amir__s.p.g
[+]  Telegram   : https://t.me/Amir_cybery
====================================================      
\033[1;91m

Your Public IP Address
=====================\033[1;96m
'''
print ip


#addres


print'''
\033[1;94m
         [1] Nmap
         ======================
         [2] Payload
         ======================
         [3] DDOS Attack
         ======================
         [4] Web Tools
         ======================
         [5] Termux OS
         ======================
         [6] Password Tools
         ======================
         [7] Cracking
         ======================
         [8] Evil Codes
         ======================
         [99] Exit
\033[1;m
'''

print ("  ")

#input-x

x = input("LammerTV=>  ")

if x == 1:
   os.system("python2 modules/nmap/nmap.py")
if x == 2:
   os.system("python2 modules/payload/payload.py")
if x == 3:
   os.system("python2 modules/ddos/ddos.py")
if x == 4:
   os.system("python2 modules/webtools/webtools.py")
if x == 5:
   os.system("python2 modules/os/os.py")
if x == 6:
   os.system("python2 modules/password/password.py")
if x == 7:
   os.system("python2 modules/crack/crack.py")
if x == 8:
   os.system("python2 modules/evilcode/evilcode.py")

























