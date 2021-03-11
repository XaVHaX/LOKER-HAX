# -*- coding: utf-8 -*-
from userinfo import *
from passinfo import *
from time import sleep
from getpass import getpass
import sys,os

B = "\033[1;34m";
WI = "\033[2;37;40m";
YM = "\033[0;33;40m";
Y = "\033[1;33m";
WM = "\033[0;37m";
G = "\033[1;32m";
W = "\033[1;0m";
R = "\033[1;31m";
GR = "\033[0;32m";
C = "\033[1;36m";
M = "\033[0;35m";
DG ="\033[1;30m";
CM = "\033[0;36m"

def loading() :
        print "Try to Login",
        type =".....\n"
        for char in type :
                sleep(0.5)
                sys.stdout.write(char)
                sys.stdout.flush()


print G+"┌──────────────────────"+W+"BETA"+G+"──────────────────────┐"
print G+"│"+R+"  ##       "+W+" #######   "+R+" ######   "+W+"####  "+R+"##    ##  "+G+"│"
print G+"│"+R+"  ##       "+W+"##     ##  "+R+"##    ##  "+W+" ##   "+R+"###   ##  "+G+"│"
print G+"│"+R+"  ##       "+W+"##     ##  "+R+"##        "+W+" ##   "+R+"####  ##  "+G+"│"
print G+"│"+R+"  ##       "+W+"##     ##  "+R+"##   #### "+W+" ##   "+R+"## ## ##  "+G+"│"
print G+"│"+R+"  ##       "+W+"##     ##  "+R+"##    ##  "+W+" ##   "+R+"##  ####  "+G+"│"
print G+"│"+R+"  ##       "+W+"##     ##  "+R+"##    ##   "+W+"##   "+R+"##   ###  "+G+"│"
print G+"│"+R+"  ######## "+W+" #######   "+R+" ######   "+W+"####  "+R+"##    ##  "+G+"│"
print G+"└───────────────────────"+W+"v1"+G+"───────────────────────┘"
print G+"Welocome To Termux, Please Login !"


loop = 'true'
while loop == 'true' :
	try:
		nm = raw_input(WM+'['+Y+'?'+WM+'] '+R+'Username '+Y+': '+WM)
		ps = getpass(WM+"["+Y+"?"+WM+"] "+R+"Password "+Y+": "+WM)
		if nm == user :
			if ps == passw :
				sleep(2)
				loading()
				print G+"Success Login as %s" % nm
				loop = 'false'
				sleep(2)
			else :
				sleep(2)
				loading()
				print G+"Wrong Password"
		else :
			sleep(2)
			loading()
			print G+"Username or Password not include"
			loop = 'true'
	except EOFError :
                print "\nCannot Close Login\n"
                loop = 'true'
	except :
		print "Cannot Close Login"
		loop = 'true'
