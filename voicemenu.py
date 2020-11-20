import os
import getpass
import speech_recognition as sr
k = sr.Recognizer()

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
	\tspeak to configure docker conatiner: 
	\tspeak to configure webserver:
	\tspeak to configure Ansible:
	\tspeak to list linux basic commands:
	\tspeak to configure hadoop:                             		
	\tspeak to create a  partiton:
	\tspeak to create a AWS instance:
	\tspeak to run data science prediction software:
	\tspeak 9 to exit:
	""")
	
	#ch = input("enter your choice : ")
	if r=="remote":
		os.system(" espeak-ng 'hello and welcome to the menu ,  i am your voice assistant' ")
		with sr.Microphone() as source:
				print("start saying ..... ")
				audio=k.listen(source)
				print("ok done ....")
		ab=k.recognize_google(audio)		
		ip=input("enter destination ip :")
		if ("configure" in ab) or ("docker" in ab) or ("container" in ab): 
			while True:
				
				os.system("tput setaf 3")
				print()
				print("speak to install docker : ")
				print("speak to create docker conatainer :")
				print("speak show all container status : ")
				print("speak to start existing containers  : ")
				print("speak download an OS image for docker : ")
				print("speak remove an docker container : ")
				print("speak to exit : ")
				print()
				
				with sr.Microphone() as source:
					print("start saying ..... ")
					audio1=k.listen(source)
					print("ok done ....")
				ab1=k.recognize_google(audio1)
					
				if ("docker" in ab1) and ("install" in ab1):
					os.system(""" ssh {} 'echo  -e "[docker123]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable\ngpgcheck=0" > /etc/yum.repos.d/dockerpractice.repo' """.format(ip)) 
					os.system("ssh {} yum install docker-ce --nobest".format(ip))
					os.system("ssh {} systemctl start docker".format(ip))
					os.system("ssh {} systemctl enable docker".format(ip))
				elif ("create" in ab1) and ( ("docker" in ab1) or ("container" in ab1) ) :
					os.system("ssh {} docker pull centos".format(ip))
					os.system("ssh {} docker run -it centos:latest".format(ip))
				elif ("status" in ab1) and ( ("container" in ab1) or ("show" in ab1) ):
					os.system("docker ps -a")
				elif ("start" in ab1) and ( ("conatiner" in ab1) or ("existing" in ab1) or ("docker" in ab1)):
					os.system("dokcer ps -a ")
					strt=input("enter the image id to start :")
					os.system("docker start {} ".format(strt))
					os.system("docker attach {} ".format(strt))
				elif ("download" in ab1) and ( ("OS" in ab1) or ("docker" in ab1) or ("image" in ab1)):
					osd=input("enter OS name")
					os.system("docker pull {}".format(osd))
				elif ("remove" in ab1) and ( ("docker" in ab1) or ("container" in ab1) ):
					os.system("dokcer ps -a ")
					strt1=input("enter the image id to delete :")
					os.system("docker rm {} ".format(strt1))
				elif ("exit" in ab1):
					#exit()
					os.system("ssh {} mkdir practice345".format(ip))
				input("press enter to continue :")	
		elif int(ch) == 2:
			os.system("tput setaf 3")
			while True: 
				#os.system("clear")
				print("""\n\tpress 1 to install httpd webserver :\n\tpress 2 to start httpd webserver :\n\tpress 3 to sop httpd webserver :\n\tpress 4 to exit :""")
				htp=input("enter your choice:  ")
				if int(htp)==1:
					os.system("ssh {} yum install httpd".format(ip))  
				elif int(htp)==2:
					os.system("ssh {} systemctl start httpd".format(ip))
				elif int(htp)==3:
					os.system("ssh {} sytemctl stop httpd".format(ip))
				elif int(htp)==4:
					exit()
				else: 
					print("invalid choice")
				input("press enter to continue :")	
		elif int(ch) == 3:
			while True: 
				#os.system("clear")
				print("""\n\tpress 1 to install Ansible :\n\tpress 2 to configure Ansible :\n\tpress 3 to create an Inventory :\n\tpress 4 to exit :""")
				htp=input("enter your choice:  ")
				if int(htp)==1:
					os.system("ssh {} pip3 install ansible".format(ip))  
				elif int(htp)==2:
					os.system("ssh {} touch ansible-inventory.txt".format(ip))  
					os.system("ssh {} mkdir /etc/ansible".format(ip))  
					os.system(""" ssh {} 'echo  -e "[defaults]\ninventory=/root/ansible-inventory.txt" > /etc/ansible/ansible.cfg' """.format(ip))
				elif int(htp)==3:
					ip1=input("enter ip: ")
					usr=input("enter username: ")
					pswd=input("enter password: ")
					os.system(""" ssh {} 'echo " {} ansible_user={} ansible_ssh_pass={} ansible_connection=ssh" > /root/hello-ansible.txt' """.format(ip,ip1,usr,pswd))
				elif int(htp)==4:
					exit()
				else: 
					print("invalid choice")
				input("press enter to continue :")		
			 
		elif int(ch) == 4:
			print("""\nifconfig : this command shows us the ip of the diffrent network card installed in our OS\n""")
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
		os.system(" espeak-ng 'hello and welcome to the menu ,  i am your voice assistant' ")
		with sr.Microphone() as source:
				print("start saying ..... ")
				audio=k.listen(source)
				print("ok done ....")
		ab=k.recognize_google(audio)
		
		if ("configure" in ab) or ("docker" in ab) or ("container" in ab): 
			while True:
				
				os.system("tput setaf 3")
				print()
				print("speak to install docker : ")
				print("speak to create docker conatainer :")
				print("speak show all container status : ")
				print("speak to start existing containers  : ")
				print("speak download an OS image for docker : ")
				print("speak remove an docker container : ")
				print("speak to exit : ")
				print()
				
		
					
				with sr.Microphone() as source:
					print("start saying ..... ")
					audio1=k.listen(source)
					print("ok done ....")
				ab1=k.recognize_google(audio1)
					
				if ("docker" in ab1) and ("install" in ab1):
					os.system(""" 'echo -e "[docker123]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0" > /etc/yum.repos.d/dockerpractice.repo' """) 
					os.system("yum install docker-ce --nobest")
					os.system("systemctl start docker")
					os.system("systemctl enable docker")
				elif ("create" in ab1) and ( ("docker" in ab1) or ("container" in ab1) ) :
					os.system("docker pull centos")
					os.system("docker run -it centos:latest ")
				elif ("status" in ab1) and ( ("container" in ab1) or ("show" in ab1) ):
					os.system("docker ps -a")
				elif ("start" in ab1) and ( ("conatiner" in ab1) or ("existing" in ab1) or ("docker" in ab1)):
					os.system("dokcer ps -a ")
					strt=input("enter the image id to start :")
					os.system("docker start {} ".format(strt))
					os.system("docker attach {} ".format(strt))
				elif ("download" in ab1) and ( ("OS" in ab1) or ("docker" in ab1) or ("image" in ab1)):
					osd=input("enter OS name")
					os.system("docker pull {}".format(osd))
				elif ("remove" in ab1) and ( ("docker" in ab1) or ("container" in ab1) ):
					os.system("dokcer ps -a ")
					strt1=input("enter the image id to delete :")
					os.system("docker rm {} ".format(strt1))
				elif ("exit" in ab1):
					exit()
				else:
					print("invalid input:")
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
			while True: 
				#os.system("clear")
				print("""\n\tpress 1 to install Ansible :\n\tpress 2 to configure Ansible :\n\tpress 3 to create an Inventory :\n\tpress 4 to exit :""")
				htp=input("enter your choice:  ")
				if int(htp)==1:
					os.system("pip3 install ansible")  
				elif int(htp)==2:
					os.system("touch ansible-inventory.txt")  
					os.system("mkdir /etc/ansible")  
					os.system(""" 'echo  -e "[defaults]\ninventory=/root/ansible-inventory.txt" > /etc/ansible/ansible.cfg' """.format(ip))
				elif int(htp)==3:
					ip1=input("enter ip: ")
					usr=input("enter username: ")
					pswd=input("enter password: ")
					os.system("{} echo ansible_user={} ansible_ssh_pass={} ansible_connection=ssh > /root/hello-ansible.txt ".format(ip1,usr,pswd))
				elif int(htp)==4:
					exit()
				else: 
					print("invalid choice")
				input("press enter to continue :")		
			 
		elif int(ch) == 4:
			print("""\nifconfig : this command shows us the ip of the diffrent network card installed in our OS \n""")
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
		exit()			
	input("press enter to continue :")
os.system("tput setaf 7")




