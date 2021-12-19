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


cmd_list = [
    "sudo apt-get update -y && upgrade -y",
    "sudo apt-get install openjdk-11-jdk",
    "sudo wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -",
    "echo deb http://pkg.jenkins.io/debian-stable binary/  | sudo tee /etc/apt/sources.list.d/jenkins.list",
    "sudo apt-get install jenkins",
    "sudo service jenkins restart",
    "sudo apt-get install nginx -y",
    "sudo apt-get install docker -y",
    "sudo apt-get install docker-compose -y"
    "sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null",
    "sudo chmod +x /usr/local/bin/docker-compose",
    "sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose",
    "sudo service docker start",
    "usermod -aG docker jenkins"
]

for i in cmd_list:
    os.system(i)
port_change()
