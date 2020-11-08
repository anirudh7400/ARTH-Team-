import os

def takeCommand():
	query=input("Enter----->")
	return query

while True:

	print("Press enter to continue...")
	n=input("")
	os.system("clear")
	print("\n\t"+42*"-")
	print("\t\t\tDocker Menu")
	print("\n\t"+42*"-")
	print("\n\tSelect an option: \n")

	print("\t1. Install Docker tool")
	print("\t2. Show running Containers")
	print("\t3. Show all Containers")
	print("\t4. Confirm Docker installed")
	print("\t5. Show Docker status")
	print("\t6. Start Docker servicces")
	print("\t7. Enable Docker services")
	print("\t8. Docker Version")
	print("\t9. Docker Info")
	print("\t10. Pull an Image")
	print("\t11. Show all the Images")
	print("\t12. Launch the Docker container")
	print("\t13. Stop Docker services")
	print("\t14. Disable Docker services")
	print("\t15. Attach Docker container")
	print("\t16. Remove Docker container")
	print("\t17. Delete an Image")
	print("\t18. Commit Docker container")
	print("\t19. Docker manual")
	print("\t20. Docker Image manual")
	print("\t21. Docker container manual")
	print("\t22. Exit")	
	print()
	
	ch=int(input("Enter your Choice:"))

	if ch == 1:
		os.system("clear")
		print("*****************")
		if not os.system("rpm -q docker-ce"):
			print("\tDocker is already installed..")
		else:
			print("\tInstalling Docker...")
			f=open("/etc/yum.repos.docker.d/docker-ce.repo","a")
			docrepo="[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0\n"
			f.write(docrepo)
			f.close()
		os.system("yum install docker-ce")
		os.system("systemctl enable docker")
		os.system("systemctl start docker")
		os.system("sleep 2")
		print("*****************")

	elif ch == 2:
		os.system("clear")
		print("*****************")
		os.system("docker ps | less")
		print("Above are the running Containers")
		print("*****************")
		
	elif ch == 3:
		os.system("clear")
		print("*****************")
		os.system("docker ps -a | less")
		print("*****************")

	elif ch == 4:
		os.system("clear")
		print("*****************")
		os.system("rpm -q docker-ce")
		print("*****************")

	elif ch == 5:
		os.system("clear")
		print("*****************")
		os.system("systemctl status docker")
		print("*****************")

	elif ch == 6:
		os.system("clear")
		print("*****************")
		os.system("systemctl start docker")
		print("*****************")

	elif ch == 7:
		os.system("clear")	
		print("*****************")	
		os.system("systemctl enable docker")
		print("*****************")

	elif ch == 8:
		print("*****************")
		os.system("clear")
		os.system("docker version")
		print("*****************")

	elif ch == 9:
		print("*****************")
		os.system("clear")		
		os.system("docker info | less")
		print("*****************")

	elif ch == 10: 
		print("*****************")
		os.system("clear")
		print("Enter the Image name--->")		
		img=takeCommand()
		os.system("docker pull "+img)
		print("Your "+img+" image is been downloaded")
		print("*****************")

	elif ch == 11: 
		print("*****************")		
		os.system("clear")
		os.system("docker images")
		print("*****************")

	elif ch == 12:
		print("*****************")
		os.system("clear")
		print("This are your available Images:-")
		os.system("docker images")
		print("Which Image should i choose..?")
		imgs=takeCommand()
		print("Your new OS is been launched")
		os.system("docker run -i -t "+imgs)		
		print("*****************")
	
	elif ch == 13: 
		print("*****************")	
		os.system("clear")
		os.system("systemctl stop docker")
		print("*****************")

	elif ch == 14:
		print("*****************")
		os.system("clear")
		os.system("systemctl disable docker")
		print("*****************")

	elif ch == 15:
		print("*****************")
		os.system("clear")
		print("This are all the running and stopped OS:-")
		os.system("docker ps -a")
		print("Which OS should i choose..?")
		os=takeCommand()
		os.system("docker attach "+os)
		print("You are attached to this particular OS")
		print("*****************")

	elif ch == 16:
		print("*****************")
		os.system("clear")
		print("This are all the running and stopped OS:-")
		os.system("docker ps -a")
		print("Which OS should i choose..?")
		os=takeCommand()
		os.system("docker rm "+os)
		print("This particular OS is been removed permanentely")
		print("*****************")

	elif  ch == 17:
		print("*****************")
		os.system("clear")
		print("This are all the Images:-")
		os.system("docker images")
		print("Which image should i choose..?")
		im=takeCommand()
		os.system("docker rmi "+im)
		print("This particular image is been removed permanentely")
		print("*****************")

	elif ch == 18: 
		print("*****************")
		os.system("clear")
		print("This are all the Containers available:-")
		os.system("docker ps -a")
		print("Which OS should i choose to Commit..?")
		com=takeCommand()
		print("Enter the name of this new image:-")
		img=takeCommand()
		os.system("docker commit "+com+" "+img)
		print("Your OS is been commited successfully")
		print("*****************")

	elif ch == 19:
		print("*****************")
		os.system("clear")
		os.system("docker --help")
		print("*****************")

	elif ch == 20: 
		print("*****************")
		os.system("clear")
		os.system("docker image --help")
		print("*****************")

	elif ch == 21:
		print("*****************")
		os.system("clear")
		os.system("docker container --help")
		print("*****************")

	elif ch == 22:
		os.system("clear")
		break

	else:
		os.system("clear")
		print("Please enter a valid option...")
						
				











































































































