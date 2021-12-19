import sys
import os
# 아직은 스크립트형으로 실행시키지만
# 진행상황에 따라서 함수형으로 만들어야됨.


def port_change():

    # 운영체제 확인
    if os.name == "nt":
        path = "./nginx"  # 테스트용
    else:
        print("i'm linux")
        path = "/etc/nginx"
    sub_path = "location.d"
#
    # 경로가 존재하지 않으면 경로를 만듦
    if not os.path.isdir(f"{path}/{sub_path}"):
        try:
            os.mkdir(f"{path}/{sub_path}")
        except:
            print("error")
    # 파일 카피
    static = open("./init/init_config", "r", encoding='utf8')
    dynamic = open(f"{path}/{sub_path}/location.conf", "w", encoding='utf8')
    for i in static:
        dynamic.write(i)
    static.close()
    dynamic.close()
#######
    config = open("./init/init_nginx.conf", "r", encoding='utf-8')
    target = open(f"{path}/nginx.conf", "w", encoding='utf-8')
    for i in config:
        target.write(i)
    config.close()
    target.close()
    os.system("sudo systemctl reload nginx")


    # 이 스크립트가 메인으로 실행 될 때
    # config파일을 세팅하고.
    # nginx 재실행 시킴.
if __name__ == "__main":
    port_change()
    os.system("sudo systemctl reload nginx")
