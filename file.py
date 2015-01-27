#!/usr/bin/python
# -*- coding: utf-8 -*-

fich=open("/etc/passwd","r")
user_num=fich.readlines()
print "El numero de usuarios en este ordenador es: " + str(len(user_num))
fich.close()

fich=open("/etc/passwd","r")

for user in user_num:
    
	conf = user.split(":");
	username = conf[0]
	shell = conf[-1]
	print "El usuario: *" + username + "* utiliza la shell: " + shell

fich.close()

