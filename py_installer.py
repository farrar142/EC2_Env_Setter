import os
import locale
import subprocess
import time
from py_nginx_setter import *


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

# 우분투 20부터 snap을 사용하기 때문에 사용하지 않음.


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


system_list = [
    "sudo apt-get update -y && upgrade -y",
    "sudo apt-get install openjdk-11-jdk -y"
]
jenkins_list = [
    "sudo wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -",
    "echo deb http://pkg.jenkins.io/debian-stable binary/  | sudo tee /etc/apt/sources.list.d/jenkins.list",
    "sudo apt-get install jenkins -y",
    "sudo service jenkins start"
]

nginx_list = [
    "sudo apt-get update",
    "sudo apt-get install nginx -y",
]
docker_list = [
    "sudo apt-get update",
    "sudo snap install docker",
    "sudo addgroup --system docker",
    "sudo adduser jenkins docker",
    "sudo snap disable docker"
    "sudo snap enable docker",
    "sudo curl -L https://github.com/docker/compose/releases/download/1.24.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null",
    "sudo chmod +x /usr/local/bin/docker-compose",
    "sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose",
    "sudo service docker start",
    "sudo usermod -aG docker jenkins"
    "sudo usermod -aG docker $(whoami)"
]
swap_list = [
    "sudo fallocate -l sizeM /swapfile",
    "sudo dd if=/dev/zero of=/swapfile bs=sizeM count=32",
    "sudo chmod 600 /swapfile",
    "sudo mkswap /swapfile",
    "sudo swapon /swapfile",
    "sudo swapon -s",
]

# 인스톨기능


def install(list):
    for i in list:
        print(f"\n{i}\n")
        os.system(i)
        # time.sleep(3)


def install_all():
    print("운영체제 최신화")
    install(system_list)
    while (os.popen("systemctl | grep jenkins.service").read() == ""):
        print("젠킨스 설치")
        install(jenkins_list)
    while (os.popen("systemctl | grep nginx.service").read() == ""):
        print("nginx 설치")
        install(nginx_list)
    while (os.popen("snap list | grep docker").read() == ""):
        print("도커 설치")
        install(docker_list)

# 젠킨스 초기 비밀번호


def get_jenkins_pwd():
    return os.popen("sudo cat /var/lib/jenkins/secrets/initialAdminPassword").read()

# ssh키 만들기


def make_ssh():
    os.system("sudo mkdir /var/lib/jenkins/.ssh")
    id = input("id 를 입력하세요 ) ")
    name = input("key 이름을 입력하세요 ) ")
    os.system(
        f"sudo ssh-keygen -t rsa -b 4096 -C \"{id}\" -f /var/lib/jenkins/.ssh/{name}")
    os.system("\n")
    os.system("\n")

# ssh키 확인


def key_list():
    keys = os.popen("ls /var/lib/jenkins/.ssh").read().split("\n")
    keys = list(filter(None, keys))
    for index, i in enumerate(keys):
        print(f"{index} 번 : {i}")
    print("확인 하려는 파일을 입력해주세요")
    print("종료 하려면 아무키")
    key_ans = input("번호 ) ")
    try:
        print("")
        os.system(f"sudo cat /var/lib/jenkins/.ssh/{str(keys[int(key_ans)])}")
        print("")
    except:
        return


def swap_file():
    print("스왑 파일 영역의 크기를 입력하세요 단위 MB")
    size = input("입력 ) ")
    try:
        size = int(size)
    except:
        return
    for i in swap_list:
        if "size" in i:
            i = i.replace("size", str(size))
        print(f"\n{i}\n")
        os.system(i)


if __name__ == "__main__":
    all = os.popen("uname -v").read()
    _all = all.split(" ")[0].split("-")[0].split("~")[1].split(".")

    print(f"current os version = \n{all}\n")
    if int(_all[0]) < 20:
        if int(_all[1]) < 4:
            print("23~20.04-1 이상의 버전이 필요합니다.")
            exit()

    while True:
        print("원하는 작업을 선택하세요")
        print("1.전체설치, 2.nginx 설정 3.jenkins 초기화 번호 4.젠킨스 ssh 키 만들기 5.젠킨스 ssh 확인 6.스왑파일 설정")
        print("종료 하려면 아무키")
        answer = input("번호 ) ")
        if answer == "1":
            install_all()
        elif answer == "2":
            port_change()
        elif answer == "3":
            get_jenkins_pwd()
        elif answer == "4":
            make_ssh()
        elif answer == "5":
            key_list()
        elif answer == "6":
            swap_file()
        else:
            exit()
