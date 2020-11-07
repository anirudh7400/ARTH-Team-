import os
import getpass
os.system("tput setaf 3")
print("\t\t\t\tWELCOME TO MY MENU !!!!!!!!!!!!")
os.system("tput setaf 2")
pw=getpass.getpass("enter your password:  ")
if pw!="arth":
	print("incorrect password. ")
	exit()
r = input("where you want to run your program (local/remote) :")

os.system("tput setaf 6")
while True:
	os.system("clear")
	print("""	
	\tpress 1 to create docker conatiner: 
	\tpress 2 to configure webserver:
	\tpress 3 to configure Ansible:
	\tpress 4 to list linux basic commands:
	\tpress 5 to configure hadoop:                             		
	\tpress 6 to create a  partiton:
	\tpress 7 to create a AWS instance:
	\tpress 8 to run data science prediction software:
	\tpress 9 to exit:
	""")
	ch = input("enter your choice : ")
	if r=="remote":
		ip = input("enter destination IP: ")
		if int(ch) == 1:
			os.system("ssh {} date".format(ip))  
		elif int(ch) == 2:
			os.system("date")  
		elif int(ch) == 3:
			os.system("date")  
		elif int(ch) == 4:
			os.system("date")  
		elif int(ch) == 9:
			exit()  
# yum install httpd
# systemctl start httpd

	elif r=="local":
		if int(ch) == 1:
			os.system("date")  
		elif int(ch) == 2:
			os.system("systemctl status httpd")  
			os.system("systemctl start httpd")  
		elif int(ch) == 3:
			os.system("date")  
		elif int(ch) == 4:
			os.system("date")  
		elif int(ch) == 9:
			exit()  

	else:
		print("invalid choice")			
	input("press enter to continue :")
os.system("tput setaf 7")




