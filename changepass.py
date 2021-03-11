from passinfo import *
from time import sleep
import os
print "Do You Sure Want Change Password ?"
sure = raw_input('Y/N : ')
sleep(1)
if sure == 'Y' or sure == 'y' :
	loop = 'true'
	while loop == 'true' :
		old = raw_input('Old Password : ')
		sleep(1)
		if old == passw :
			loop = 'false'
			new = raw_input('Input New Password : ')
			lup = 'true'
			while lup == 'true' :
				now = raw_input('Confirm New Password : ')
				sleep(1)
				if now == new :
					lup = 'false'
					os.remove('passinfo.py')
					os.system('touch passinfo.py')
					w = open('passinfo.py','a')
					w.write("passw='%s'\n" % now )
					w.close()
					print "[*] New Password add Succesfully"
				else :
					print "[*] New Password is incorrect"
					lup = 'true'
		else :
			print "[!] Wrong Password (CTRL + D for close)"
			loop = 'true'
else :
	print "Okay"
	exit()
