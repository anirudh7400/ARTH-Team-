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
			while True:
				#os.system("clear")
				print("press 1 to install docker : ")
				print("press 2 to create docker conatainer :")
				print("press 3 to exit : ")
				dock=input("enter your choice :")
				if int(dock)==1:
					os.system(""" ssh {} "echo  -e "[docker123]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable\ngpgcheck=0" > /etc/yum.repos.d/dockerpractice.repo" """.format(ip)) 
					os.system("ssh {} yum install docker-ce --nobest".format(ip))
					os.system("ssh {} systemctl start docker".format(ip))
					os.system("ssh {} systemctl enable docker".format(ip))
				elif int(dock)==2:
					os.system("ssh {} docker pull centos".format(ip))
					os.system("ssh {} docker run -it centos:latest".format(ip))
				else:
					exit()
				input("press enter to continue :")	
		elif int(ch) == 2:
			os.system(""" ssh {} "echo  "hello\nworld" > /etc/yum.repos.d/abc1223.repo" """.format(ip))  
		elif int(ch) == 3:
			os.system("date")  
		elif int(ch) == 4:
			os.system("date")  
		elif int(ch) == 5:
			os.system("date")  
		elif int(ch) == 6:
			os.system("date")  
		elif int(ch) == 7:
			os.system("date")  
		elif int(ch) == 8:
			os.system("date")  
		elif int(ch) == 9:
			exit()  


	elif r=="local":
		if int(ch) == 1:
			while True:
				#os.system("clear")
				print("press 1 to install docker : ")
				print("press 2 to create docker conatainer :")
				print("press 3 to exit : ")
				dock=input("enter your choice :")
				if int(dock)==1:
					os.system("""echo -e "[docker123]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0" > dockerpractice.repo""") 
				elif int(dock)==2:
					os.system("docker pull centos")
					os.system("docker run -it centos:latest ")
				else:
					exit()
				input("press enter to continue :")	
		elif int(ch) == 2:
			os.system("tput setaf 3")
			while True: 
				#os.system("clear")
				print("""\n\tpress 1 to install httpd webserver :\n\tpress 2 to start httpd webserver :\n\tpress 3 to sop httpd webserver :\n\tpress 4 to exit :""")
				htp=input("enter your choice:  ")
				if int(htp)==1:
					os.system("yum install httpd")  
				elif int(htp)==2:
					os.system("systemctl start httpd")
				elif int(htp)==3:
					os.system("sytemctl stop httpd")
				elif int(htp)==4:
					exit()
				else: 
					print("invalid choice")
				input("press enter to continue :")		
		elif int(ch) == 3:
			os.system("date")  
		elif int(ch) == 4:
			os.system("date")  
		elif int(ch) == 5:
			os.system("date")  
		elif int(ch) == 6:
			os.system("date")  
		elif int(ch) == 7:
			os.system("date")  
		elif int(ch) == 8:
			os.system("date")  
		elif int(ch) == 9:
			exit()  

	else:
		print("invalid choice")			
	input("press enter to continue :")
os.system("tput setaf 7")




