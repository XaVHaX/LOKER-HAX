from os import system
from time import sleep

print "[*] Try To Build Login Termux"
sleep(2)
system('mv .login.py $PREFIX/etc/')
system('mv bash.bashrc $PREFIX/etc/')
system('mv userinfo.py $PREFIX/etc/')
system('mv adduser.py $PREFIX/etc/')
system('mv passinfo.py $PREFIX/etc/')
system('mv changepass.py $PREFIX/etc/')
print "[*] Successfully"
sleep(1)
system('cd $HOME')
system('bash')
