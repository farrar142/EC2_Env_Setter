###

sudo mkdir /home/pyscript && cd /home/pyscript
sudo git clone https://github.com/farrar142/EC2_Env_Setter .
or
sudo git clone "porked repository" .
sudo python3 py_installer.py

### nginx설정을 바꾸고 싶을땐

1. https://github.com/farrar142/EC2_Env_Setter 리포지터리를 포크 한 후.
2. init폴더의 nginx.conf와 location.conf의 내용을 변경한 후
3. git pull origin master
4. EC2에서 git clone "porked repository" .
5. sudo python3 py_nginx_setter.py
