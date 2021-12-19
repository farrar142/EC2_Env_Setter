import os
import locale
import subprocess
from setter import *


def get_logs(cmd):
    os_encoding = locale.getpreferredencoding()
    #print("System Encdoing :: ", os_encoding)
    if os_encoding.upper() == 'cp949'.upper():  # Windows
        return subprocess.Popen(
            cmd, stdout=subprocess.PIPE).stdout.read().decode('utf-8').strip()
    elif os_encoding.upper() == 'UTF-8'.upper():  # Mac&Linux
        return os.popen(cmd).read()
    else:
        print("None matched")
        exit()


def get_cpu_info():
    if os.name == "nt":
        return os.popen("echo %PROCESSOR_ARCHITECTURE%").read().lower()
    elif os.name == "posix":
        return os.popen("dpkg --print-architecture").read().lower()


def get_docker_repo():
    type = get_cpu_info()
    if type == "amd64":
        # cpu가 x86_64 또는 amd64계열일 경우
        os.system("echo \"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null")

    elif type == "armhf":
        # cpu가 armhf계열일 경우
        os.system("echo \"deb [arch=armhf signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | sudo tee / etc/apt/sources.list.d/docker.list > /dev/null")
    elif type == "arm64":
        # cpu가 arm64계열일 경우
        os.system("echo \"deb [arch=arm64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | sudo tee / etc/apt/sources.list.d/docker.list > /dev/null")


cmd_list1 = [
    "sudo apt-get update -y && upgrade -y",
    "sudo apt-get install openjdk-11-jdk",
    "sudo wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -",
    "echo deb http://pkg.jenkins.io/debian-stable binary/  | sudo tee /etc/apt/sources.list.d/jenkins.list",
    "sudo apt-get install jenkins -y",
    "sudo service jenkins restart",
    "sudo apt-get install nginx -y",
    "sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release",
    "sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-ketring.gpg",
]
cmd_list2 = [
    "sudo pat-get update",
    "sudo apt-get install docker-ce docker-ce-cli containerd.io -y"
    "sudo apt-cache madison docker-ce docker-ce-cli -y"
    "sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null",
    "sudo chmod +x /usr/local/bin/docker-compose",
    "sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose",
    "sudo service docker start",
    "usermod -aG docker jenkins"

]

for i in cmd_list1:
    print(i)
    os.system(i)
get_docker_repo()
for i in cmd_list2:
    print(i)
    os.system(i)
port_change()
