import os 
import subprocess

def takeCommand():
	query=input("Enter----->")
	return query

while True:
	
	print("Press enter to continue...")
	n=input("")
	os.system("clear")
	print("\n\t"+42*"-")
	print("\t\t\tMENU")
	print("\n\t"+42*"-")
	print("\n\tSelect an option: \n")

	print("\t1. AWS Menu")
	print("\t2. Docker Menu")
	print("\t3. Exit")
	
	n=int(input("Enter your Choice:"))

	if n == 1:
		def require() :
			print("Checking requirements..")
			x=subprocess.getstatusoutput("aws --version")
			if x[0] !=0:
				print("AWS cli software is not installed in your system")
				print("For continuing forwad please install aws cli")
				ch=input("press [y/n] =")
				if ch == "y" or ch == "Y" :
					os.system("sudo pip3 install awscli --force-reinstall --upgrade")
					require()
				else:
					print("Aws cli is required to run aws commands")
			else:
				print("Aws cli is installed on your system... ")
				print("Everthing is fine..")
				print("Configure the aws cli...")
				os.system("aws configure")
		require()

		while True:
			print()
			print("\t1. Create a Key pair")
			print("\t2. Create a Security group")
			print("\t3. Launch an Instance")
			print("\t4. Create an EBS Volume")
			print("\t5. Attach the EBS Volume")
			print("\t6. Create a Bucket in S3")
			print("\t7. Remove the Bucket from S3")
			print("\t8. Put Object in a Bucket")
			print("\t9. Remove Object from the Bucket")
			print("\t10. Create a CLoud Front distribution")
			print("\t11. Start any Instance")
			print("\t12. Describe any Instance")
			print("\t13. Describe Key pairs")
			print("\t14. Describe Volumes")
			print("\t15. Describe Security Groups")
			print("\t16. Create a Snapshot")
			print("\t16. Exit")
			print()

			ch=int(input("Enter your Choice--->"))
	
			if ch == 1:
				print("*****************")
				key=input("Enter the name of your key--->")
				os.system("aws ec2 create-key-pair --key-name "+key+" --output text > "+key+".pem")
				print("*****************")
			elif ch == 2:
				print("*****************")
				g_name=input("Enter the name of your Security Group--->")
				os.system("aws ec2 create-security-group --group-name "+g_name+" --description "+g_name)
				print("Your new Security-Group is created")
				print("*****************")
			elif ch == 3:
				print("*****************")
				print("As your account is of Free-Tier these are the free eligible images:")
				print()
				print("Choose the AMI(image) name--->")
				speak("Choose the AMI image name:")
				print("1)Amazon Linux 2 AMI")
				print("2)Amazon Linux AMI")
				print("3)Red Hat Enterprise Linux 8")
				print("4)SUSE Linux Enterprise Server 15 SP2")
				print("5)Ubuntu Server 20.04 LTS")
				print("6)Ubuntu Server 18.04 LTS")
				print("7)Microsoft Windows Server 2019 Base")
				print()
				am=input("Enter that specific no.:")
				if am=="1":
					ami="ami-0947d2ba12ee1ff75"
					print("Amazon Linux 2 AMI is been selected")
				elif am=="2":
					ami="ami-032930428bf1abbff"
					print("Amazon Linux AMI is been selected")
				elif am=="3":
					ami="ami-098f16afa9edf40be"
					print("Red Hat Enterprise Linux 8 is been selected")
				elif am=="4":
					ami="ami-0a782e324655d1cc0"
					print("SUSE Linux Enterprise Server 15 SP2 is been selected")
				elif am=="5":
					ami="ami-0dba2cb6798deb6d8"
					print("Ubuntu Server 20.04 LTS is been selected")
				elif am=="6":
					ami="ami-0817d428a6fb68645"
					print("Ubuntu Server 18.04 LTS is been selected")
				elif am=="7":
					ami="ami-0eb7fbcc77e5e6ec6"
					print("Microsoft Windows Server 2019 Base is been selected")
				else:
					print("Enter the right number...")	
				print()
				print("Choosing an Instance type t2.micro----->")
				print()
				print("Configuring Instance Details----->")
				print()
				i_no=input("Enter the number of Instances:")
				
				print("Bydefault choosing the subnet or you want to choose----->")
				s=takeCommand()
				if s=="yes":
					print("Choose the Subnet:")
					speak("Choose the Subnet:")
					print()
					print("1)Default Virginia us-east-1a")
					print("2)Default Virginia us-east-1b")
					print("3)Default Virginia us-east-1c")
					print("4)Default Virginia us-east-1d")
					print("5)Default Virginia us-east-1e")
					print("6)Default Virginia us-east-1f")
					print()
					sub=input("Enter that specific no.:")
					if sub=="1":
						sub="subnet-8w9b33ec"
						print("Default Virginia us-east-1a is been selected")
					elif sub=="2":
						sub="subnet-4c09be6d"
						print("Default Virginia us-east-1b is been selected")
					elif sub=="3":
						sub="subnet-50cbb31d" 
						print("Default Virginia us-east-1c is been selected")
					elif sub=="4":
						sub="subnet-fe2095a1" 
						print("Default Virginia us-east-1d is been selected")
					elif sub=="5":
						sub="subnet-5a9b646b" 
						print("Default Virginia us-east-1e is been selected")
					elif sub=="6":
						sub="subnet-53e88a5d" 
						print("Default Virginia us-east-1f is been selected")
					else:
						print("Enter the right no...")				
				else:
					sub="subnet-5a9b646b"
					print("Ok, choosing bydefault subnet")
				print()
				security=input("Enter the name of your existing security group----->")
					
				print("Selecting "+security+" Security Group id for this instance")
				print()				
				key=input("Enter the name of your key----->")
					
				print("Your existing key named "+key+" is been selected for creating this instance")
				os.system("aws ec2 run-instances --image-id "+ami+" --instance-type t2.micro --count "+i_no+" --key-name "+key+" --security-groups "+security)
				print("Your Instance has been successfully Launched")
				print("*****************")
				print()

			elif ch == 4:
				print("*****************")
				print("Note: Size must be restricted to 5 Gib to keep you bounded in free-tier")
				size=input("Enter the Size:")
				zone=input("Enter the Zone:")
				os.system("aws ec2 create-volume --volume-type gp2 --size "+size+" --availability-zone "+zone)
				print("Your EBS Volume is been created")	
				print("*****************")
				print()

			elif ch == 5:
				print("*****************")
				v_id=input("Enter your Volume Id:")
				i_id=input("Enter your Instance Id:")
				print("Attaching please wait...")
				os.system("aws ec2 attach-volume --volume-id "+v_id+" --instance-id "+i_id+" --device /dev/sdf")
				print("Successfully Attached")
				print("*****************")
				print()

			elif ch == 6:
				print("*****************")
				b_name=input("Enter the name of Bucket:")
				os.system("aws s3api create-bucket --bucket "+b_name+" --region us-east-1")
				print("Your new Bucket named "+b_name+" in your default N.Virginia Region")
				print("*****************")
			
			elif ch == 7:
				print("*****************")
				print("Enter the name of your existing Bucket:")
				b_name=input()
				os.system("aws s3api delete-bucket --bucket "+b_name+" --region us-east-1")
				print("Your Bucket named "+b_name+" is been removed successfully")
				print("*****************")
 
			elif ch == 8:
				print("*****************")
				b_name=input("Enter the name of Bucket:")
				ob_name=input("Enter the Object:")
				loc=input("Enter the directory where your object is been situated:")
				os.system("aws s3api put-object --bucket "+b_name+" --key "+ob_name+" --body "+loc+" --acl public-read")
				print("Your Object is now in your bucket")
				print("*****************")

			elif ch == 9:
				print("*****************")
				b_name=input("Enter the name of your existing Bucket:")
				o_name=input("Enter the object you want to remove:")
				os.system("aws s3api delete-object --bucket "+b_name+" --key "+o_name)
				print("Your Object is been removed successfully")
				print("*****************")

			elif ch == 10:
				print("*****************")
				d_name=input("Enter the origin domain name:")
				os.system("aws cloudfront create-distribution --origin-domain-name "+d_name)
				print("Your distribution is been created")				
				print("*****************")
		
			elif ch == 11:
				print("*****************")
				id=input("Enter the instance id:")
				os.system("aws ec2 start-instances --instance-ids "+id)
				print("Your instance is now started")
				print("*****************")

			elif ch == 12:
				print("*****************")
				os.system("aws ec2 describe-instances")
				print("This are your instances")
				print("*****************")

			elif ch == 13:
				print("*****************")
				os.system("aws ec2 describe-key-pairs ")
				print("This are the allready existing key pairs")
				print("*****************")

			elif ch == 14:
				print("*****************")
				os.system("aws ec2 describe-volumes")
				print("this are your volumes")
				print("*****************")

			elif ch == 15:
				print("*****************")
				os.system("aws ec2 describe-security-groups")
				print("This are your security groups")
				print("*****************")

			elif ch == 16:
				print("*****************")
				des=input("Enter the description:")
				v_id=input("Enter the Volume Id:")
				os.system("aws ec2 create-snapshot --volume-id "+v_id+" --description "+des)
				print("*****************")

			elif ch == 17:
				print("*****************")
				print("Exited from AWS Command Executer")
				break

			else:
				print("Please enter the valid option....")
		
	elif n == 2:
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

		else ch == 3:
			print("Exiting...")
			break
		else:
			print("Please enter a valid option....")
							
				





















	