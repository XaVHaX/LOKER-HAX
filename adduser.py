# -*- coding: utf-8 -*-
import os
from getpass import getpass
from time import sleep
os.system('toilet -f standard LOKER --gay')
WM = "\033[0;37m";
G = "\033[1;32m";
T = "\033[0;32m";
W = "\033[1;0m";
R = "\033[1;31m";
print R+"["+WM+"√"+R+"]"+WM+" Author	"+R+":"+WM+" Xavier Hax"
print R+"["+WM+"√"+R+"]"+WM+" Team	"+R+":"+WM+" Sicx Brother"
print W+"═════════════════════════════════"
print G+"["+R+"!"+G+"]"+WM+" This is LOgin maKER"+G+" v.1"
print G+"["+R+"?"+G+"]"+WM+" Input username for new user"
user = raw_input(G+'Username[] : '+W)
sleep(1)
print G+"["+W+"*"+G+"] "+WM+"Adding new user '%s'" % user
sleep(2)
print G+"["+W+"*"+G+"] "+WM+"Success"
pasw = getpass(G+'Input New Termux Password[] : '+W)
sleep(2)
scpw = 'true'
while scpw == 'true' :
	repasw = getpass(G+'Confirm New Termux Password[] : '+W)
	if repasw == pasw :
		sleep(2)
		print G+"["+W+"*"+G+"]"+WM+" passwd: password add successfully"
		scpw = 'false'
	else :
		sleep(2)
		print G+"["+R+"!"+G+"]"+WM+" passwd: pasword is incorrect"
		scpw = 'true'
print "Next running build.py"
print "$ python2 build.py"
os.remove('userinfo.py')
os.system('touch userinfo.py')
x = open('userinfo.py','a')
x.write("user='%s'\n" % user)
x.close()
os.remove('passinfo.py')
os.system('touch passinfo.py')
z = open('passinfo.py','a')
z.write("passw ='%s'\n" % repasw)
z.close()
os.remove('bash.bashrc')
os.system('touch bash.bashrc')
y = open('bash.bashrc','a')
y.write('#!/bin/bash\n')
y.write('if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then\n')
y.write('\tcommand_not_found_handle() {\n')
y.write('\t\t/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"\n')
y.write('\t}\n')
y.write('fi\n\n')
y.write('adduser(){\n')
y.write('\tpython2 $PREFIX/etc/adduser.py\n')
y.write('}\n')
y.write('userinfo(){\n')
y.write('\tcat $PREFIX/etc/userinfo.py\n')
y.write('}\n')
y.write('changepass(){\n')
y.write('\tpython2 changepass.py\n}\n')
y.write('clear\n')
y.write('python2 .login.py\n')
y.write('clear\n')
y.write('toilet --gay -f big %s\n'% user)
y.write('neofetch\n')
y.write("PS1='\e[0;37m┌─\e[1;37m[\e[0;36mroot\e[0;37m@\e[1;31m"+user+"\e[1;37m]\e[1;30m\w\\n\e[0;37m└─╼\e[1;31m$ \e[0;32m'")
y.close()

