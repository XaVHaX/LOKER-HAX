#!/bin/bash
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
	command_not_found_handle() {
		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
	}
fi

adduser(){
	python2 $PREFIX/etc/adduser.py
}
userinfo(){
	cat $PREFIX/etc/userinfo.py
}
changepass(){
	python2 changepass.py
}
clear
python2 .login.py
clear
toilet --gay -f big hax
neofetch
PS1='\e[0;37m┌─\e[1;37m[\e[0;36mroot\e[0;37m@\e[1;31mhax\e[1;37m]\e[1;30m\w\n\e[0;37m└─╼\e[1;31m$ \e[0;32m'